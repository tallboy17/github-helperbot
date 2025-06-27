Repository: nvbn/thefuck
Language: Python
Stars: 92445
Forks: 3711
-----
*The Fuck* is a magnificent app, inspired by a [@liamosaur](https://twitter.com/liamosaur/)
[tweet](https://twitter.com/liamosaur/status/506975850596536320),
that corrects errors in previous console commands.  
Is *The Fuck* too slow? [Try the experimental instant mode!](#experimental-instant-mode)  
[![gif with examples][examples-link]][examples-link]  
More examples:  
```bash
➜ apt-get install vim
E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)
E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?

➜ fuck
sudo apt-get install vim [enter/↑/↓/ctrl+c]
[sudo] password for nvbn:
Reading package lists... Done
...
```  
```bash
➜ git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

git push --set-upstream origin master


➜ fuck
git push --set-upstream origin master [enter/↑/↓/ctrl+c]
Counting objects: 9, done.
...
```  
```bash
➜ puthon
No command 'puthon' found, did you mean:
Command 'python' from package 'python-minimal' (main)
Command 'python' from package 'python3' (main)
zsh: command not found: puthon

➜ fuck
python [enter/↑/↓/ctrl+c]
Python 3.4.2 (default, Oct  8 2014, 13:08:17)
...
```  
```bash
➜ git brnch
git: 'brnch' is not a git command. See 'git --help'.

Did you mean this?
branch

➜ fuck
git branch [enter/↑/↓/ctrl+c]
* master
```  
```bash
➜ lein rpl
'rpl' is not a task. See 'lein help'.

Did you mean this?
repl

➜ fuck
lein repl [enter/↑/↓/ctrl+c]
nREPL server started on port 54848 on host 127.0.0.1 - nrepl://127.0.0.1:54848
REPL-y 0.3.1
...
```  
If you're not afraid of blindly running corrected commands, the
`require_confirmation` [settings](#settings) option can be disabled:  
```bash
➜ apt-get install vim
E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)
E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?

➜ fuck
sudo apt-get install vim
[sudo] password for nvbn:
Reading package lists... Done
...
```