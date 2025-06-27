Repository: soimort/you-get
Language: Python
Stars: 55751
Forks: 9759
-----
You may specify an HTTP proxy for `you-get` to use, via the `--http-proxy`/`-x` option:  
```
$ you-get -x 127.0.0.1:8087 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
```  
However, the system proxy setting (i.e. the environment variable `http_proxy`) is applied by default. To disable any proxy, use the `--no-proxy` option.  
**Tips:**  
* If you need to use proxies a lot (in case your network is blocking certain sites), you might want to use `you-get` with [proxychains](https://github.com/rofl0r/proxychains-ng) and set `alias you-get="proxychains -q you-get"` (in Bash).
* For some websites (e.g. Youku), if you need access to some videos that are only available in mainland China, there is an option of using a specific proxy to extract video information from the site: `--extractor-proxy`/`-y`.