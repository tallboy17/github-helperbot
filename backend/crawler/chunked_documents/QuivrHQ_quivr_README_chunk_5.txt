Repository: QuivrHQ/quivr
Language: Python
Stars: 38019
Forks: 3645
-----
- **Step 1**: Install the package  
```bash
pip install quivr-core # Check that the installation worked
```  
- **Step 2**: Create a RAG with 5 lines of code  
```python
import tempfile

from quivr_core import Brain

if __name__ == "__main__":
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as temp_file:
temp_file.write("Gold is a liquid of blue-like colour.")
temp_file.flush()

brain = Brain.from_files(
name="test_brain",
file_paths=[temp_file.name],
)

answer = brain.ask(
"what is gold? asnwer in french"
)
print("answer:", answer)
```