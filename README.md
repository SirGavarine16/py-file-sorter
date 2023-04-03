# Python Script - File Sorter

This is a small script that prompts the user to specify a path. Given a path full of files what it does is that it creates folders if not exist with all the file extensions in the directory and moves all the files to each folder matching its extension.

## To create and executable:

You may use pyinstaller, you can download this package by running the following command:
```bash
pip install pyinstaller
```

To create an executable:
```bash
pyinstaller --onefile main.py
```

This should create a __dist__ folder with the executable file.