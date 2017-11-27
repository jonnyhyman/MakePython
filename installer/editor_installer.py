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
"""

from win32com.client import Dispatch
from subprocess import Popen, PIPE
from tempfile import mktemp
from zipfile import ZipFile
import utilities as utils
from shutil import rmtree
import install_globals
import urllib.request
import platform
import winshell
import sys
import os

def add_to_log(farg, *args, end='\n'):

    x = ''.join([str(farg)+' '] + [ str(arg)+' ' for arg in args ])

    with open('INSTALL.log','a') as f:
        f.write(' ' + str(x) + end)

print = add_to_log

class install:
    def __init__(self, ui):

        """
            This is the install handler for the makepython editor.
            There are a few basic steps:
                1. Download makepython distribution for this system
                2. Unpack it into Python's site-packages
                3. Prepend system PATH with makepython.executable's path
                4. Change sys defaults to prefer makepython on .py files
                5. Create shortcuts

        """

        self.ui = ui
        self.prog = 0

        if self.ui.uninstall:  # if uninstalling,
            return

        self.py_dir = self.ui.core_installer.target_dir  # use same python!
        self.mp_dir = self.py_dir + '\\Lib\\site-packages\\makepython'


        if self.ui.system == 'Windows':

            self.zip_nam = install_globals.zip_nam
            self.zip_url = install_globals.zip_url

            self.windows_install()

        else:
            self.unix_install()

    def download_and_extract(self):
        """ Download the zip package and install it into site-packages """

        if not os.path.isdir(self.mp_dir):
            print('making directory:',self.mp_dir)
            os.makedirs(self.mp_dir)
            print('makedirs done!')
        else:
            print('found makepython directory. Deleting for update...')
            self.ui.installbutton.setText("UPDATING")
            rmtree(self.mp_dir)

        if os.path.isfile('./' + self.zip_nam + '.zip'):
            print('removing',self.zip_nam)
            os.remove('./' + self.zip_nam + '.zip')

        print('downloading from',self.zip_url)
        urllib.request.urlretrieve( self.zip_url, self.zip_nam + '.zip' )
        print('download done!')

        try:

            print('unzipping...',self.zip_nam + '.zip into',self.mp_dir)

            zipfile = ZipFile(self.zip_nam + '.zip')
            zipfile.extractall(self.mp_dir)
            zipfile.close()

        except Exception as e:
            print('download_and_extract exception! : ',e)
            sys.exit()

        # Cleanup, clean up everybody do your share!

        if os.path.isfile('./' + self.zip_nam + '.zip'):
            print('removing',self.zip_nam)
            os.remove('./' + self.zip_nam + '.zip')

    def ensure_dependencies(self):
        """
            This function installs all pip dependencies
        """

        self.prc = []

        for dir_name, dependency in install_globals.pip_dependencies.items():

            print('ensuring dependency :',dependency)

            folder = self.py_dir + '\\Lib\\site-packages\\' + dir_name

            # assumes if the directory exists, there's stuff inside!
            if os.path.isdir(folder):
                print(dependency,'installed. Yay!')

            else:

                if self.ui.system == 'Windows':
                    pip_path = self.py_dir + '\\Scripts\\pip.exe'
                else:
                    pip_path = self.py_dir + '\\Scripts\\pip'

                process_args = [pip_path, 'install', dependency]

                print('   ', process_args)

                # forward shell to current process
                self.prc += [Popen(process_args, shell=True)]

    def windows_install(self):
        """ Install on Microsoft Windows """

        # ---------------------------------- Main Editor install

        self.ensure_dependencies()
        self.download_and_extract()
        self.prog = 50

        #---------------------------------- PATH configuration

        utils.set_env_path(append_to_path=self.mp_dir)
        print('appended', self.mp_dir ,'to PATH')
        self.prog = 75

        #--------------------------------------- Additional os-specific setup

        # if running win8, there is a windows bug that prevents proper startup.
        # send the user a message to notify they'll need to restart

        # CAUSE = (
        # "https://superuser.com/questions/593949/why-wont-my-windows-8-command"
        # "line-update-its-path"
        # )

        if '8' in platform.win32_ver()[0]:
            self.ui.sendmessage("Due to a Microsoft Windows 8 bug, you should"
                                " reboot after installation everything to work"
                                " correctly. Sorry!")

        # create desktop and start menu shortcuts

        desktop = winshell.desktop()
        startmenu = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu'

        for target in ( desktop, startmenu ):

            target = os.path.join(target, "Make Python.lnk")

            if not os.path.isfile(target):
                shell = Dispatch('WScript.Shell')
                short = shell.CreateShortCut(target)

                short.Targetpath = self.mp_dir + '\\makepython.exe'
                short.WorkingDirectory = desktop
                short.IconLocation = short.Targetpath
                short.save()

        # create context menu item
        utils.set_context_menu(self.mp_dir + '\\makepython.exe')

        self.prog = 96

    def launch_after_install(self):

        """ Launch by cmd line """

        if self.ui.system == 'Windows':
            launch_command = self.mp_dir+'\\makepython.exe'

        else:
            launch_command = self.mp_dir+'\\makepython'

        launch_command = [launch_command,'launch='+self.mp_dir]

        print('launching',launch_command)
        self.ui.close()

        with Popen( launch_command,
                    shell=True, env=os.environ,
                    stdin=PIPE,
                    stderr=PIPE,
                    stdout=PIPE) as p: # launch it!

            print('--------------------------',end='')
            print(' LAUNCHED INSTANCE STDOUT ',end='')
            print('--------------------------')
            print(p.stdout.read().decode('utf-8'),end='')

        print('--------------------------',end='')
        print(' LAUNCHED INSTANCE EXITED ',end='')
        print('--------------------------')

    def uninstall(self, mp_dir):

        if self.ui.system == 'Windows':
            """ Install on Microsoft Windows """

            self.mp_dir = mp_dir

            # ---------------------------------- Main Editor uninstall

            print('deleted', self.mp_dir)
            rmtree(self.mp_dir)

            #---------------------------------- PATH deletion

            utils.set_env_path(delete_from_path=self.mp_dir)
            print('deleted', self.mp_dir ,'from PATH')

            #--------------------------------------- Additional os-specific setup

            # delete desktop and start menu shortcuts

            desktop = winshell.desktop()
            startmenu = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu'

            for target in ( desktop, startmenu ):

                target = os.path.join(target, "Make Python.lnk")

                if os.path.isfile(target):
                    os.remove(target)

            # delete context menu item
            utils.set_context_menu(self.mp_dir + '\\makepython.exe', undo=True)

            self.ui.installbutton.setText("REMOVED. BYE BYE!")

    def progress(self):
        """ Check progress of install """

        if (all([ prc.poll() is not None for prc in self.prc ])
            and self.prog == 96):

            # signal that we're truly done

            return 100

        else:

            return self.prog
