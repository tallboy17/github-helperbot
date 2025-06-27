Repository: oobabooga/text-generation-webui
Language: Python
Stars: 44003
Forks: 5671
-----
Very fast setup that should work on any Python 3.9+:  
```bash
# Clone repository
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies (choose appropriate file under requirements/portable for your hardware)
pip install -r requirements/portable/requirements.txt

# Launch server (basic command)
python server.py --portable --api --auto-launch

# When done working, deactivate
deactivate
```
</details>  
<details>
<summary>
Manual full installation with conda or docker
</summary>