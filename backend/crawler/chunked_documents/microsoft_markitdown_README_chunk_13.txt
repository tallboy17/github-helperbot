Repository: microsoft/markitdown
Language: Python
Stars: 59294
Forks: 3083
-----
- Navigate to the MarkItDown package:  
```sh
cd packages/markitdown
```  
- Install `hatch` in your environment and run tests:  
```sh
pip install hatch  # Other ways of installing hatch: https://hatch.pypa.io/dev/install/
hatch shell
hatch test
```  
(Alternative) Use the Devcontainer which has all the dependencies installed:  
```sh
# Reopen the project in Devcontainer and run:
hatch test
```  
- Run pre-commit checks before submitting a PR: `pre-commit run --all-files`