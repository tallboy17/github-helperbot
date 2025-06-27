Repository: nvbn/thefuck
Language: Python
Stars: 92445
Forks: 3711
-----
The following rules are enabled by default on specific platforms only:  
* `apt_get` &ndash; installs app from apt if it not installed (requires `python-commandnotfound` / `python3-commandnotfound`);
* `apt_get_search` &ndash; changes trying to search using `apt-get` with searching using `apt-cache`;
* `apt_invalid_operation` &ndash; fixes invalid `apt` and `apt-get` calls, like `apt-get isntall vim`;
* `apt_list_upgradable` &ndash; helps you run `apt list --upgradable` after `apt update`;
* `apt_upgrade` &ndash; helps you run `apt upgrade` after `apt list --upgradable`;
* `brew_cask_dependency` &ndash; installs cask dependencies;
* `brew_install` &ndash; fixes formula name for `brew install`;
* `brew_reinstall` &ndash; turns `brew install <formula>` into `brew reinstall <formula>`;
* `brew_link` &ndash; adds `--overwrite --dry-run` if linking fails;
* `brew_uninstall` &ndash; adds `--force` to `brew uninstall` if multiple versions were installed;
* `brew_unknown_command` &ndash; fixes wrong brew commands, for example `brew docto/brew doctor`;
* `brew_update_formula` &ndash; turns `brew update <formula>` into `brew upgrade <formula>`;
* `dnf_no_such_command` &ndash; fixes mistyped DNF commands;
* `nixos_cmd_not_found` &ndash; installs apps on NixOS;
* `pacman` &ndash; installs app with `pacman` if it is not installed (uses `yay`, `pikaur` or `yaourt` if available);
* `pacman_invalid_option` &ndash; replaces lowercase `pacman` options with uppercase.
* `pacman_not_found` &ndash; fixes package name with `pacman`, `yay`, `pikaur` or `yaourt`.
* `yum_invalid_operation` &ndash; fixes invalid `yum` calls, like `yum isntall vim`;  
The following commands are bundled with *The Fuck*, but are not enabled by
default:  
* `git_push_force` &ndash; adds `--force-with-lease` to a `git push` (may conflict with `git_push_pull`);
* `rm_root` &ndash; adds `--no-preserve-root` to `rm -rf /` command.