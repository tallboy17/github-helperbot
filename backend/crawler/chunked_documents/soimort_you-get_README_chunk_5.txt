Repository: soimort/you-get
Language: Python
Stars: 55751
Forks: 9759
-----
You may either download the [stable](https://github.com/soimort/you-get/archive/master.zip) (identical with the latest release on PyPI) or the [develop](https://github.com/soimort/you-get/archive/develop.zip) (more hotfixes, unstable features) branch of `you-get`. Unzip it, and put the directory containing the `you-get` script into your `PATH`.  
Alternatively, run  
```
$ cd path/to/you-get
$ [sudo] python -m pip install .
```  
Or  
```
$ cd path/to/you-get
$ python -m pip install . --user
```  
to install `you-get` to a permanent path. (And don't omit the dot `.` representing the current directory)  
You can also use the [pipenv](https://pipenv.pypa.io/en/latest) to install the `you-get` in the Python virtual environment.  
```
$ pipenv install -e .
$ pipenv run you-get --version
you-get: version 0.4.1555, a tiny downloader that scrapes the web.
```