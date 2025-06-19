import os
import json

chunked_folder = "chunked_documents"
metadata_path = os.path.join("github_documents", "metadata.json")

# Load metadata
with open(metadata_path, "r", encoding="utf-8") as f:
    metadata_list = json.load(f)
metadata_map = {m["readme_file"].replace(".md", ""): m for m in metadata_list}

for filename in os.listdir(chunked_folder):
    if filename.endswith(".txt"):
        # Infer the base README name (without _chunk_X.txt)
        base = filename.rsplit("_chunk_", 1)[0]
        # Try to find metadata
        meta = metadata_map.get(base, {})
        meta_str = (
            f"Repository: {meta.get('repo_name', 'N/A')}\n"
            f"Language: {meta.get('language', 'N/A')}\n"
            f"Stars: {meta.get('stars', 'N/A')}\n"
            f"Forks: {meta.get('forks', 'N/A')}\n"
            "-----\n"
        )
        chunk_path = os.path.join(chunked_folder, filename)
        with open(chunk_path, "r", encoding="utf-8") as f:
            content = f.read()
        with open(chunk_path, "w", encoding="utf-8") as f:
            f.write(meta_str + content)

print("Metadata added to all chunked documents.") 