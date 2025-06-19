import faiss
import numpy as np
import google.generativeai as genai
import os
import json
import logging

# --- 0. Load Configuration (Temporary for logging setup) ---
# Load config quickly to get logging setting before full setup
temp_config_path = "config.json"
temp_config = {}
try:
    with open(temp_config_path, 'r', encoding='utf-8') as f:
        temp_config = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    pass # Handle errors gracefully, use default logging if config not found

# --- Configure Logging ---
log_level = logging.INFO if temp_config.get('application', {}).get('enable_logging', True) else logging.CRITICAL
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- 0. Load Configuration (Full Load) ---
def load_config(config_path="config.json"):
    """Loads configuration from a JSON file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        logger.info(f"Configuration loaded from {config_path}")
        return config
    except FileNotFoundError:
        logger.error(f"Error: Config file not found at {config_path}. Please create it.")
        exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON config file: {e}")
        exit(1)

config = load_config()

# Get settings from config
EMBEDDING_MODEL = config['api_settings']['gemini_embedding_model']
DOCUMENTS_FOLDER = config['document_loading']['documents_folder']
ALLOWED_EXTENSIONS = tuple(config['document_loading']['allowed_file_extensions'])
FAISS_INDEX_TYPE = config['faiss_index_settings']['faiss_index_type']
FAISS_INDEX_FILE = config['faiss_index_settings']['index_file_name']
MAPPING_FILE = config['faiss_index_settings']['mapping_file_name']

logger.info(f"Using Gemini embedding model: {EMBEDDING_MODEL}")
logger.info(f"Documents will be loaded from: {DOCUMENTS_FOLDER} (Extensions: {', '.join(ALLOWED_EXTENSIONS)})")
logger.info(f"FAISS index file: {FAISS_INDEX_FILE}")
logger.info(f"Mapping file: {MAPPING_FILE}")

# --- 1. Load Documents from a Folder (returning ID and content) ---
def load_documents_with_ids(folder_path, allowed_extensions):
    """
    Loads text files from a specified folder, returning a list of (document_id, content) tuples.
    Here, document_id is the filename.
    """
    loaded_docs_with_ids = []
    document_contents = [] # Also keep a separate list for batch embedding
    doc_ids_for_mapping = [] # To map FAISS index to our document_id

    if not os.path.isdir(folder_path):
        logger.error(f"Error: Document folder '{folder_path}' not found. Please create it and add your text files.")
        return [], [], []

    logger.info(f"Loading documents from: {folder_path}")
    for filename in os.listdir(folder_path):
        if filename.endswith(allowed_extensions):
            filepath = os.path.join(folder_path, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # We'll use the filename as the unique document ID
                    doc_id = filename
                    loaded_docs_with_ids.append({"id": doc_id, "content": content})
                    document_contents.append(content)
                    doc_ids_for_mapping.append(doc_id)
                logger.info(f"  Loaded: {filename}")
            except Exception as e:
                logger.error(f"  Error reading file {filename}: {e}")
    return loaded_docs_with_ids, document_contents, doc_ids_for_mapping

# --- 2. Build FAISS Index and Mapping ---
def build_faiss_index_and_mapping(all_document_contents, all_doc_ids, model_name, index_type):
    """Generates embeddings, builds a FAISS index, and creates a FAISS ID to Document ID mapping."""
    if not all_document_contents:
        logger.warning("No documents to build index from.")
        return None, None, None

    logger.info(f"Generating embeddings for {len(all_document_contents)} documents using Gemini...")
    try:
        response = genai.embed_content(model=model_name, content=all_document_contents)
        document_embeddings = np.array(response['embedding'], dtype='float32')
        dimension = document_embeddings.shape[1]
        logger.info(f"Generated embeddings with dimension: {dimension}")
        logger.info(f"Embeddings shape: {document_embeddings.shape}")

    except Exception as e:
        logger.error(f"Error generating embeddings with Gemini API: {e}. Check API key and model access.")
        return None, None, None

    logger.info(f"Creating FAISS index of type: {index_type}")
    faiss_index = None
    if index_type == "IndexFlatL2":
        faiss_index = faiss.IndexFlatL2(dimension)
    else:
        logger.warning(f"Unknown FAISS_INDEX_TYPE '{index_type}'. Defaulting to IndexFlatL2.")
        faiss_index = faiss.IndexFlatL2(dimension)

    if faiss_index:
        faiss_index.add(document_embeddings)
        logger.info(f"Added {faiss_index.ntotal} vectors to the FAISS index.")

    # Create the FAISS ID to Document ID mapping
    # The list index directly corresponds to the FAISS internal ID
    faiss_id_to_doc_id_map = all_doc_ids
    
    return faiss_index, faiss_id_to_doc_id_map, dimension

# --- 3. Save FAISS Index and Mapping ---
def save_faiss_artifacts(faiss_index_obj, faiss_map_list, index_file, map_file):
    """Saves the FAISS index and the FAISS ID to Document ID mapping."""
    try:
        faiss.write_index(faiss_index_obj, index_file)
        logger.info(f"FAISS index saved to {index_file}")

        with open(map_file, 'w', encoding='utf-8') as f:
            json.dump(faiss_map_list, f, indent=4)
        logger.info(f"FAISS ID to Document ID mapping saved to {map_file}")
        return True
    except Exception as e:
        logger.error(f"Error saving FAISS artifacts: {e}")
        return False

# --- Main Execution for Index Creation ---
if __name__ == "__main__":
    logger.info(f"Starting {config['application']['app_name']} Index Creator...")

    # Load documents and their IDs
    loaded_docs_with_ids, document_contents, doc_ids_for_mapping = load_documents_with_ids(DOCUMENTS_FOLDER, ALLOWED_EXTENSIONS)

    if not document_contents:
        logger.error("No documents found to create index. Exiting.")
        exit(1)

    # Build the FAISS index and create the mapping
    faiss_index, faiss_id_to_doc_id_map, _ = build_faiss_index_and_mapping(
        document_contents, doc_ids_for_mapping, EMBEDDING_MODEL, FAISS_INDEX_TYPE
    )

    if faiss_index:
        # Save the FAISS index and the mapping
        if save_faiss_artifacts(faiss_index, faiss_id_to_doc_id_map, FAISS_INDEX_FILE, MAPPING_FILE):
            logger.info("Index creation and saving complete.")
        else:
            logger.error("Failed to save FAISS index or mapping.")
    else:
        logger.error("Failed to build FAISS index.")

    logger.info("Index Creator finished.")