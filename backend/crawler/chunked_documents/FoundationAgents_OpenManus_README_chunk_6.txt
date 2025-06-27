Repository: FoundationAgents/OpenManus
Language: Python
Stars: 46956
Forks: 8199
-----
1. Install uv (A fast Python package installer and resolver):  
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```  
2. Clone the repository:  
```bash
git clone https://github.com/FoundationAgents/OpenManus.git
cd OpenManus
```  
3. Create a new virtual environment and activate it:  
```bash
uv venv --python 3.12
source .venv/bin/activate  # On Unix/macOS
# Or on Windows:
# .venv\Scripts\activate
```  
4. Install dependencies:  
```bash
uv pip install -r requirements.txt
```