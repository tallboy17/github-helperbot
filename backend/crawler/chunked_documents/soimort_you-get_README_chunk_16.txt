Repository: soimort/you-get
Language: Python
Stars: 55751
Forks: 9759
-----
Use the `--output-dir`/`-o` option to set the path, and `--output-filename`/`-O` to set the name of the downloaded file:  
```
$ you-get -o ~/Videos -O zoo.webm 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
```  
**Tips:**  
* These options are helpful if you encounter problems with the default video titles, which may contain special characters that do not play well with your current shell / operating system / filesystem.
* These options are also helpful if you write a script to batch download files and put them into designated folders with designated names.