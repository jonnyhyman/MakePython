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

from subprocess import Popen, call
import utilities as utils
import install_globals
import urllib.request
import platform
import os

from PyQt5 import QtCore

def add_to_log(farg, *args):

    x = ''.join([str(farg)+' '] + [ str(arg)+' ' for arg in args ])

    with open('INSTALL.log','a') as f:
        f.write(' ' + str(x) + '\n')

print = add_to_log

class installThread(QtCore.QThread):

    def setCommands(self,cmds):
        self.cmds = cmds

    def run(self):

        if self.cmds is not None:
            print('calling >>', ''.join([cmd+' ' for cmd in self.cmds]))
            self.prc = Popen(self.cmds)
            #self.prc.wait()
        else:
            self.prc = False

class install:
    def __init__(self,Vn,Rn,Ui):

        """
            This is the install handler for Python.
            There are a few basic steps:
                1. Download the proper Python installer from python.org
                2. Install (and provide progress updates)
                3. Cleanup

        """

        self.ui = Ui

        if self.ui.system == 'Windows':
            self.target_dir = ''.join(['C:\\Python',(Vn),(Rn)[:Rn.index('.')]])

            if platform.machine().lower() == 'amd64':
                self.target_dir += '-64'
            else:
                self.target_dir += '-32'

            executable_name = 'python-'+str(Vn)+'.'+str(Rn)

            if platform.machine().lower() == 'amd64':
                self.executing = executable_name  + '-amd64.exe'
                command = [self.executing]
            else:
                self.executing = executable_name  + '.exe'
                command = [self.executing]

            command += ['/quiet']
            command += ['PrependPath=1']
            command += ['TargetDir='+self.target_dir]

            # Check for python in path and in target folder
            if ((os.path.isfile(self.target_dir + '\\python') or
                 os.path.isfile(self.target_dir + '\\python.exe'))
                and self.target_dir in os.environ['Path']):

                print('found a pre-existing target python...',end='')

                if self.ui.uninstall:
                    print('uninstalling from', self.target_dir)
                    return self.target_dir

            else:

                if self.ui.uninstall:  # if uninstalling,
                    print('target python not installed')
                    return None        # signal that makepython not installed

            # As long as we're not uninstalling, always run python installer
            if not self.ui.uninstall:
                print('getting python installer')
                self.get_installer(Vn,Rn)

                print('running platform_installer.make')
                self.make(command)

        elif self.ui.system == 'Mac':
            pass

        elif self.ui.system == 'Linux':
            pass

    def get_installer(self, Vn, Rn):
        """ Get the python executable installer """

        installer = self.executing

        url = install_globals.pythonorg_root
        url += str(Vn)+'.'+str(Rn)+'/'  # like 3.6.3/python-3.6.3-amd64.exe"
        url += installer

        if os.path.isfile(self.executing):
            os.remove(self.executing)

        print('downloading', url, 'as', installer)
        inst_exec = urllib.request.urlretrieve( url, installer )

    def make(self,cmd):
        """ Fork the installer from a separate thread """
        self.ithread = installThread()
        self.ithread.setCommands(cmd)
        self.ithread.run()

    def progress(self):
        """ this function evaluates the progress based on python.exe existence,
            and whether the installer process is alive.

            if python.exe is in place, return 50 percent done, else 22 percent
            if installer process exited (poll() not None), assume it's done

                --> This is a bit of a weak assumption because if the process
                    exited without actually installing things fall apart...

        """

        if (self.ithread.prc != False and self.ithread.prc.poll() is None):

            if self.ui.system == 'Windows':
                python_name = 'python.exe'
            else:
                python_name = 'python'

            if os.path.isfile(os.path.join(self.target_dir, python_name)):
                print('python.executable in place...')
                return 50
            else:
                print('installer still active...')
                return 22

        else:

            print('Python installer done, removing executable')

            if os.path.isfile(self.executing):
                os.remove(self.executing)

            return 100
