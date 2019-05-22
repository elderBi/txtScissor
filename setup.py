from cx_Freeze import setup, Executable
import sys
import os

os.environ['TCL_LIBRARY'] = r"C:\Users\Bi001\AppData\Local\Programs\Python\Python36\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Bi001\AppData\Local\Programs\Python\Python36\tcl\tk8.6" 

include_files = [r"C:\Users\Bi001\AppData\Local\Programs\Python\Python36\DLLs\tcl86t.dll",
				 r"C:\Users\Bi001\AppData\Local\Programs\Python\Python36\DLLs\tk86t.dll"]
base = 'Win32GUI' if sys.platform == 'win32' else None
options = {'packages': ['cn2an', 'tkinter', 're', 'winreg', 'os', 'docx'], "include_files": include_files}

setup(name = '<txtScissor>',
          version = "1.0",
          description = '<for my cat>',
          options = {'build_exe': options},
          executables = [Executable(script = 'txtScissor.py', 
									base = base, 
									targetName = 'txtScissor.exe', 
									icon = 'cat.ico', )])
