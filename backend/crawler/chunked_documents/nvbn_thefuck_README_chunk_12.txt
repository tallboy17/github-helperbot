Repository: nvbn/thefuck
Language: Python
Stars: 92445
Forks: 3711
-----
The default behavior of *The Fuck* requires time to re-run previous commands.
When in instant mode, *The Fuck* saves time by logging output with [script](https://en.wikipedia.org/wiki/Script_(Unix)),
then reading the log.  
[![gif with instant mode][instant-mode-gif-link]][instant-mode-gif-link]  
Currently, instant mode only supports Python 3 with bash or zsh. zsh's autocorrect function also needs to be disabled in order for thefuck to work properly.  
To enable instant mode, add `--enable-experimental-instant-mode`
to the alias initialization in `.bashrc`, `.bash_profile` or `.zshrc`.  
For example:  
```bash
eval $(thefuck --alias --enable-experimental-instant-mode)
```