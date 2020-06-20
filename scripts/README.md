Scripts
=====
As you know, **you can use the python language to create your own scripts** in an easy way. Just create your app, install a package, and run a command.

Here you can find two examples of python scripts:

* delete_files.py: Simple example to delete all files that have the provided extension
 * Subdirectories won't be scanned
 * Variables to be modified:
   * scanned_directory
   * extension_of_files_to_be_deleted (only one)


* move_files.py: Extended example to move all files with the provided extensions, from source to destination
 * All subdirectories will also be scanned
 * Variables tp be modified:
   * user_directory (you can delete it if you don't need it)
   * source_path
   * destination_path
   * extension_files (one or more)


> WARNING: you should be careful with the execution of any script


Create the executable files
-----------

1. Install PyInstaller package
```pip install pyinstaller```

2. Go to your program’s directory and run
```pyinstaller myscript.py```

 * This will generate the bundle in a subdirectory called dist. **You can move the executable files wherever you want**.


Detailed documentation about pyinstaller: https://pyinstaller.readthedocs.io/en/stable/
