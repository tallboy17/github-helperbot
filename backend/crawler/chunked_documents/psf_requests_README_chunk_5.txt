Repository: psf/requests
Language: Python
Stars: 52972
Forks: 9481
-----
When cloning the Requests repository, you may need to add the `-c
fetch.fsck.badTimezone=ignore` flag to avoid an error about a bad commit timestamp (see
[this issue](https://github.com/psf/requests/issues/2690) for more background):  
```shell
git clone -c fetch.fsck.badTimezone=ignore https://github.com/psf/requests.git
```  
You can also apply this setting to your global Git config:  
```shell
git config --global fetch.fsck.badTimezone ignore
```  
---  
[![Kenneth Reitz](https://raw.githubusercontent.com/psf/requests/main/ext/kr.png)](https://kennethreitz.org) [![Python Software Foundation](https://raw.githubusercontent.com/psf/requests/main/ext/psf.png)](https://www.python.org/psf)