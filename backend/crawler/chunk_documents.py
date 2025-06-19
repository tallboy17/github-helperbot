import os
from langchain.text_splitter import MarkdownHeaderTextSplitter

# Settings
input_folder = "github_documents"
output_folder = "chunked_documents"
os.makedirs(output_folder, exist_ok=True)

# Define the headers to split on (e.g., all markdown headers)
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
    ("####", "Header 4"),
    ("#####", "Header 5"),
    ("######", "Header 6"),
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".md"):
        with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
            text = f.read()
        chunks = splitter.split_text(text)
        for i, chunk in enumerate(chunks):
            chunk_filename = f"{os.path.splitext(filename)[0]}_chunk_{i+1}.txt"
            with open(os.path.join(output_folder, chunk_filename), "w", encoding="utf-8") as cf:
                cf.write(chunk.page_content)
print("Chunking complete! Chunks saved in", output_folder)
