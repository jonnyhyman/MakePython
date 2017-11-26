# Make Python - Editor, Installer

[Download the Latest Installer](https://github.com/jonnyhyman/MakePython/releases/download/v1.0.0/Make.Python.Installer.exe)

 ![Make Python Editor - Dark](https://github.com/jonnyhyman/MakePython/blob/master/images/dark.png?raw=true)
![Make Python Editor - Installer](https://github.com/jonnyhyman/MakePython/blob/master/images/installer.png?raw=true)

### Best Python Installer
 * Elegant design
 * Written 100% in pure Python
 * Automatic recognition of OS and 32 / 64 bit
 * Automatic installation of all editor dependencies
 * Prepends Python to PATH by default, without breaking PATH
 * Installs into obvious folders like C:\Python3x-32 or C:\Python3x-64
 * Supports Microsoft Windows 7 - 10
 	* macOS and Linux support coming very soon


 ### Powerful Python Editor


 * Simple, powerful design
 * Written 100% in pure Python
 * Runs as live Python, open to the core
 * Context "Edit with Make Python" for .py files
 * Launch the current Python file quickly (Ctrl + Enter)
 * Open interactive Python shell quickly (Ctrl + Shift + Enter)
 	* You can also select code and run it first in new interactive shell
 * Python Importable ("import makepython")
 * Syntax highlighting and brace matching, custom styles
 * Open source code of selected module or function
 * Interface to "pip install anything"
 * Line swapping (Ctrl +  Up / Down)
 * Auto newline tab matching
 * Light Mode / Dark Mode

  ![Make Python Editor - Dark](https://github.com/jonnyhyman/MakePython/blob/master/images/dark.png?raw=true)
 ![Make Python Editor - Light](https://github.com/jonnyhyman/MakePython/blob/master/images/light.png?raw=true)

 * Supports Microsoft Windows 7 - 10
 	* macOS and Linux support coming very soon

### Roadmap

* macOS and Linux support
* GitHub integration
* File refresh if file changed externally
* Text editing features
	* Group tabbing
	* Group untabbing
	* Python auto-complete
	* Better undo/redo with cursor selections
	* Fused code line numbers and scroll bar

### Editor Architecture

Make Python Editor is stored as a Python package. The editor is actually run as live interactive Python, from within an executable. This allows changes to the editor without the need to recompile!

With PyQt5 as the UI backend, the editor is extremely extensible.

 ![Editor Architecture](https://github.com/jonnyhyman/MakePython/blob/master/images/editorarch.png?raw=true)

By placing the makepython folder on environment path and in registry during install, there are a number of ways to launch.

1. Shortcut
2. Context Menu "Edit with Make Python" for .py files
3. Command Line "makepython" command or "makepython filepath.py"

 ![Editor Architecture](https://github.com/jonnyhyman/MakePython/blob/master/images/editorarch2.png?raw=true)

The green line in the above diagram denotes when the user "launches" their current Python file (Ctrl + Enter or the Py Button).

To allow development within a Python distribution that is not the one which houses Make Python, "Launching" looks for python in the entire user environment path, and launches Python with that distribution. (see diagram below)

For instance, this architecture also means you could launch your code directly into your Anaconda environment from Make Python.

  ![Editor Architecture](https://github.com/jonnyhyman/MakePython/blob/master/images/editorarch3.png?raw=true)

 In the case that makepython is not in the environment path (accidental deletion, etc...), only the command line interface is lost.

 ### License and Issue Reporting

GNU General Public License v3.0

When you find bugs, please report them to the "Issues" tab on this repo!
