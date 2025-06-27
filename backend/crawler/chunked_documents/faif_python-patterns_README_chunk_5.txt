Repository: faif/python-patterns
Language: Python
Stars: 41548
Forks: 7018
-----
Please run the following before submitting a patch
- `black .` This lints your code.  
Then either:
- `tox` or `tox -e ci37` This runs unit tests. see tox.ini for further details.
- If you have a bash compatible shell use `./lint.sh` This script will lint and test your code. This script mirrors the CI pipeline actions.  
You can also run `flake8` or `pytest` commands manually. Examples can be found in `tox.ini`.