import os
import subprocess
from github import Github
import json
import requests

# GitHub API setup
github_token = os.getenv("GITHUB_API_KEY")
if not github_token:
    raise EnvironmentError("GITHUB_API_KEY environment variable not set.")
g = Github(github_token)

temp_config_path = "config.json"
temp_config = {}
try:
    with open(temp_config_path, 'r', encoding='utf-8') as f:
        temp_config = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    pass # Handle errors gracefully, use default logging if config not found


def load_config(config_path="config.json"):
    """Loads configuration from a JSON file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        exit(1)
    except json.JSONDecodeError as e:
        exit(1)

config = load_config()

# Settings
query = config['crawler']['query'] # e.g., "lang:python stars:>1000"
output_folder = "github_documents"
os.makedirs(output_folder, exist_ok=True)


NUM_FILES = config['crawler']['num_files']
num_files = 0

# Search repositories
repositories = g.search_repositories(query=query, sort="stars", order="desc")
top_repositories = repositories[:100]

def download_file_from_url(url, output_path):
    """Downloads a file from the given URL and saves it to the specified output path."""
    #try:
    response = requests.get(url)
    response.raise_for_status()
    with open(output_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {url} to {output_path}")
    #except Exception as e:
        #print(f"Failed to download {url}: {e}")

# Store metadata for each repository
metadata_list = []

# Clone and convert repositories
for repo in top_repositories:
    repo_name = repo.full_name.replace("/", "_")
    try:
        contents = repo.get_contents("")
        for file_content in contents:
            if file_content.name == "README.md":
                d_url = file_content.download_url
                output_path = os.path.join("./github_documents", f"{repo_name}_README.md")
                download_file_from_url(d_url, output_path)
                
                # Add metadata for this repository
                metadata = {
                    "readme_file": f"{repo_name}_README.md",
                    "repo_name": repo.full_name,
                    "language": repo.language or "Unknown",
                    "stars": repo.stargazers_count,
                    "forks": repo.forks_count,
                    "description": repo.description or "",
                    "url": repo.html_url,
                    "created_at": repo.created_at.isoformat() if repo.created_at else "",
                    "updated_at": repo.updated_at.isoformat() if repo.updated_at else ""
                }
                metadata_list.append(metadata)
    except Exception as e:
        print(f"Error processing {repo_name}: {e}")

# Save metadata to JSON file
metadata_path = os.path.join(output_folder, "metadata.json")
with open(metadata_path, 'w', encoding='utf-8') as f:
    json.dump(metadata_list, f, indent=2, ensure_ascii=False)

print("GitHub crawling complete! Files saved in", output_folder)
print(f"Metadata saved to {metadata_path}")

