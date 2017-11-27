"""
    This file is part of MakePython.
    MakePython is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    HDCS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with HDCS.  If not, see <http://www.gnu.org/licenses/>.

    Make Python Editor Starter

        This file is the python source sister of the
        makepython.executable file.

        It is built by pyinstaller to distribute as executable.

        Basically, the job of this program is to ensure
        all dependencies are satisfied, and if not, to
        install them.

        If they are satisfied, then the job of this program is to
        redirect the desired files to open to the __editor__.py "live"
        python file to start the editor.

        This file assumes it is embedded BELOW the python.executable which
        is responsible for running the editor.

"""

# PyQt5 only required PRIOR to pyinstaller distribution
from utilities import get_usr_reg
import __initwin__ as initwin
from subprocess import Popen
from PyQt5 import QtWidgets
import platform
import sys
import os
import time

def get_makepython_dir():
    """ We use this to find where the current file, makepython.exe
        exists (from folders in system environment path) """

    print('looking for makepython.executable in path directories...')

    if platform.system() == 'Windows':
        path = get_usr_reg('PATH',r'Environment')

    else:
        path = os.environ['Path']

    for folder in path.split(';'):

        if platform.system() == 'Windows':
            executable = '\\makepython.exe'
        else:
            executable = '\\makepython'

        print('trying :', folder + executable)

        if os.path.isfile(folder + executable):
            print('found makepython.executable!')
            return folder

    # If we couldn't find in PATH, check each python installation

    print('Couldnt find makepython.executable in PATH dirs...')
    print('Checking in all python distributions... Looking for python.exes:')

    for folder in os.environ['Path'].split(';') + path.split(';') :

        if platform.system() == 'Windows':
            executable = '\\python.exe'
        else:
            executable = '\\python'

        print('trying :', folder + executable)

        if os.path.isfile(folder + executable):
            print('found python!')

            mk_pkg = '\\Lib\\site-packages\\makepython'

            if os.path.isdir(folder + mk_pkg):
                print('found makepython folder!',folder+mk_pkg)

                if platform.system() == 'Windows':
                    executable = '\\makepython.exe'
                else:
                    executable = '\\makepython'

                if os.path.isfile(folder + mk_pkg + executable):
                    print('found makepython.exe!',folder + mk_pkg + executable)
                    return folder + mk_pkg

                else:
                    print('''couldn't find makepython.exe :(''')
            else:
                print('could not find makepython folder...',folder+mk_pkg)

def look_up(file_to_find, current_working_directory=None):
    """ The purpose of this function is to determine what is the python
        path root in which this file exists. It is used throughout to
        ensure we use the current python distribution for running the editor,
        instead of some other distribution which may be in system path """

    ## only use if editing the proper-directory (site-packaged) makepython.py
    if current_working_directory is None:
        current_working_directory = get_makepython_dir()

    ## only use if testing from some remote directory
    #current_working_directory = 'C:\\Python36-64\\Lib\\site-packages\\makepython\\'
    #current_working_directory = 'C:\Python37-64\Lib\site-packages\makepython'
    search_directory = current_working_directory  # start here

    print('searching for',file_to_find,'above',current_working_directory)

    try:
        while not os.path.isfile(search_directory + '\\' + file_to_find):
            search_directory = search_directory[:search_directory.rindex('\\')]

    except ValueError:
        print(file_to_find+" couldn't be found anywhere above makepython.exe!")
        return None

    print('found '+file_to_find+' in', search_directory)

    return search_directory

def ensure_dependencies(py_dir):
    """
        This function ensures that the current python distribution has the
        required dependencies:

            - PyQt5
    """

    #                     path to dependent folder         : pypi name
    dependencies = {py_dir + '\\Lib\\site-packages\\PyQt5' : 'pyqt5'}

    for folder, dependency in dependencies.items():

        # assumes if the directory exists, there's stuff inside!
        if os.path.isdir(folder):
            print(dependency,'installed. Yay!')

        else:

            pip_path = py_dir + '\\Scripts\\pip'

            process_args = [pip_path, 'install', dependency]

            app = QtWidgets.QApplication(sys.argv)
            gui = initwin.InitWin('Installing '+dependency, process_args)
            gui.show()
            app.exec_()

    return True  # now that depencies are installed, return True!

if __name__ == '__main__':

    try:
        files_to_open = []
        launch_direct = None

        # if launching for the first time, path is not refreshed.
        # so the installer will provide us with the launch folder!

        if len(sys.argv) == 2 and 'launch' in sys.argv[1]:
            launch_direct = sys.argv[1].split('=')[1]  # launch=/directory/
        else:
            files_to_open = sys.argv[1:]

        if platform.system() == 'Windows':
            py_dir = look_up('python.exe', launch_direct)
            python_executable = py_dir + '\\python.exe'
        else:
            py_dir = look_up('python', launch_direct)
            python_executable = py_dir + '\\python'

        mp_dir = look_up('__editor__.py', launch_direct)

        makepython_editor = mp_dir + '\\__editor__.py'

        # Ensure pyqt bin is visible for this session
        temp_path_append = (py_dir + '\\Lib\\site-packages\\PyQt5\\Qt\\bin')
        os.environ['PATH'] = os.environ['PATH'] +';'+ temp_path_append

        if len(files_to_open) > 0:

            if ensure_dependencies(py_dir):

                for filepath in files_to_open:

                    launch_args = [python_executable, makepython_editor, filepath]

                    print('launching:',launch_args)
                    print('current python path:')
                    [print('   '+var) for var in sys.path]
                    print('current os path:')
                    [print('   '+var) for var in os.environ['Path'].split(';')]

                    # forward stdout to our current shell
                    Popen(launch_args, shell=True, env=os.environ)

        else:

            if ensure_dependencies(py_dir):

                launch_args = [python_executable, makepython_editor]

                print('launching:',launch_args)
                print('current python path:')
                [print('   '+var) for var in sys.path]
                print('current os path:')
                [print('   '+var) for var in os.environ['Path'].split(';')]

                # forward stdout to our current shell
                Popen(launch_args, shell=True, env=os.environ)

        sys.exit()

    except Exception as e:
        print('exit with exception:',e)
