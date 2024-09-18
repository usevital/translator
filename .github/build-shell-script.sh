pip install -r requirements.txt
pip install pyinstaller
pyinstaller --icon=images/icon.ico versions/terminal_gui.py
pyinstaller --icon=images/icon.ico versions/cli_args.py
