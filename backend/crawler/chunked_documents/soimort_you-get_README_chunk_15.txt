Repository: soimort/you-get
Language: Python
Stars: 55751
Forks: 9759
-----
You may use <kbd>Ctrl</kbd>+<kbd>C</kbd> to interrupt a download.  
A temporary `.download` file is kept in the output directory. Next time you run `you-get` with the same arguments, the download progress will resume from the last session. In case the file is completely downloaded (the temporary `.download` extension is gone), `you-get` will just skip the download.  
To enforce re-downloading, use the `--force`/`-f` option. (**Warning:** doing so will overwrite any existing file or temporary file with the same name!)