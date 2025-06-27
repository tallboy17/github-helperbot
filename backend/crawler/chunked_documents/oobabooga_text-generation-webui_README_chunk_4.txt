Repository: oobabooga/text-generation-webui
Language: Python
Stars: 44003
Forks: 5671
-----
For users who need additional backends (ExLlamaV3, Transformers) or extensions (TTS, voice input, translation, etc). Requires ~10GB disk space and downloads PyTorch.  
1. Clone the repository, or [download its source code](https://github.com/oobabooga/text-generation-webui/archive/refs/heads/main.zip) and extract it.
2. Run the startup script for your OS: `start_windows.bat`, `start_linux.sh`, or `start_macos.sh`.
3. When prompted, select your GPU vendor.
4. After installation, open `http://127.0.0.1:7860` in your browser.  
To restart the web UI later, run the same `start_` script.  
To reinstall with a fresh Python environment, delete the `installer_files` folder and run the `start_` script again.  
You can pass command-line flags directly (e.g., `./start_linux.sh --help`), or add them to `user_data/CMD_FLAGS.txt` (e.g., `--api` to enable the API).  
To update, run the update script for your OS: `update_wizard_windows.bat`, `update_wizard_linux.sh`, or `update_wizard_macos.sh`.  
<details>
<summary>
One-click installer details
</summary>