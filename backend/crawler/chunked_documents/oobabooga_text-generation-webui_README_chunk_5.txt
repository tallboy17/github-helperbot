Repository: oobabooga/text-generation-webui
Language: Python
Stars: 44003
Forks: 5671
-----
The script uses Miniconda to set up a Conda environment in the `installer_files` folder.  
If you ever need to install something manually in the `installer_files` environment, you can launch an interactive shell using the cmd script: `cmd_linux.sh`, `cmd_windows.bat`, or `cmd_macos.sh`.  
* There is no need to run any of those scripts (`start_`, `update_wizard_`, or `cmd_`) as admin/root.
* To install requirements for extensions, it is recommended to use the update wizard script with the "Install/update extensions requirements" option. At the end, this script will install the main requirements for the project to make sure that they take precedence in case of version conflicts.
* For automated installation, you can use the `GPU_CHOICE`, `LAUNCH_AFTER_INSTALL`, and `INSTALL_EXTENSIONS` environment variables. For instance: `GPU_CHOICE=A LAUNCH_AFTER_INSTALL=FALSE INSTALL_EXTENSIONS=TRUE ./start_linux.sh`.  
</details>  
<details>
<summary>
Manual portable installation with venv
</summary>