Repository: run-llama/llama_index
Language: Python
Stars: 42463
Forks: 6090
-----
We use poetry as the package manager for all Python packages. As a result, the
dependencies of each Python package can be found by referencing the `pyproject.toml`
file in each of the package's folders.  
```bash
cd <desired-package-folder>
pip install poetry
poetry install --with dev
```