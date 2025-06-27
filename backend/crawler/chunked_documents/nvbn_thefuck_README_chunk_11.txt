Repository: nvbn/thefuck
Language: Python
Stars: 92445
Forks: 3711
-----
If you'd like to make a specific set of non-public rules, but would still like
to share them with others, create a package named `thefuck_contrib_*` with
the following structure:  
```
thefuck_contrib_foo
thefuck_contrib_foo
rules
__init__.py
*third-party rules*
__init__.py
*third-party-utils*
setup.py
```  
*The Fuck* will find rules located in the `rules` module.