Repository: nvbn/thefuck
Language: Python
Stars: 92445
Forks: 3711
-----
To add your own rule, create a file named `your-rule-name.py`
in `~/.config/thefuck/rules`. The rule file must contain two functions:  
```python
match(command: Command) -> bool
get_new_command(command: Command) -> str | list[str]
```  
Additionally, rules can contain optional functions:  
```python
side_effect(old_command: Command, fixed_command: str) -> None
```
Rules can also contain the optional variables `enabled_by_default`, `requires_output` and `priority`.  
`Command` has three attributes: `script`, `output` and `script_parts`.
Your rule should not change `Command`.  
**Rules api changed in 3.0:** To access a rule's settings, import it with
`from thefuck.conf import settings`  
`settings` is a special object assembled from `~/.config/thefuck/settings.py`,
and values from env ([see more below](#settings)).  
A simple example rule for running a script with `sudo`:  
```python
def match(command):
return ('permission denied' in command.output.lower()
or 'EACCES' in command.output)


def get_new_command(command):
return 'sudo {}'.format(command.script)

# Optional:
enabled_by_default = True

def side_effect(command, fixed_command):
subprocess.call('chmod 777 .', shell=True)

priority = 1000  # Lower first, default is 1000

requires_output = True
```  
[More examples of rules](https://github.com/nvbn/thefuck/tree/master/thefuck/rules),
[utility functions for rules](https://github.com/nvbn/thefuck/tree/master/thefuck/utils.py),
[app/os-specific helpers](https://github.com/nvbn/thefuck/tree/master/thefuck/specific/).