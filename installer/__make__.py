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

from PyQt5 import QtCore, QtGui, QtWidgets
from time import time
from math import sin,pi
import platform_installer
import editor_installer
import install_globals
import utilities
import installer
import platform
import version
import ctypes
import sys
import os

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class Interface(QtWidgets.QMainWindow, installer.Ui_Install):

    def __init__(self,parent=None):
        """ This class runs the GUI and the install process as well """
        super(self.__class__, self).__init__()
        self.setupUi(self)
        # --------------------------------------------- set up front-end stuff
        self.message.setVisible(0)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.installbutton.pressed.connect(self.buttonpress)
        self.installbutton.released.connect(self.buttonrelease)
        self.unix_close.clicked.connect(self.close)
        self.win_close.clicked.connect(self.close)

        self.system = platform.system()

        self.color_timer = QtCore.QTimer()
        self.color_start = (0,0,0)
        self.color_stime = time()
        self.color_timer.timeout.connect(self.new_color)
        self.color_timer.start(50)

        self.progressbar.setValue(0)
        self.uninstall = False

        if self.system == 'Windows':
            self.unix_close.setVisible(0)
            self.win_close.setVisible(1)
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('make')

        else:
            self.unix_close.setVisible(1)
            self.win_close.setVisible(0)

        # --------------------------------------- Definition of install phases

        self.phases = {
                        'core'  : 0,  # install python core
                        'editor': 0,  # install python editor
                      }

        self.phase_handlers = {
                        'core'  : None,
                        'editor': None,
                        }

        self.phase_starter = {
                        'core'  : self.core_install,
                        'editor': self.editor_install,
        }

    def buttonpress(self):
        """ capture the button press time for buttonrelease to evaluate """
        self.press_time = time()

    def buttonrelease(self):
        """ if the install button is released, evaluate if we are
            installing or uninstalling, depending on the time button held """
        self.held_time = time() - self.press_time

        print('   >> button held for',self.held_time,'sec')

        if self.held_time <= 5:
            self.make()
        else:
            self.unmake()

    def unmake(self):
        """ uninstall the editor """

        self.uninstall = True
        self.installbutton.setText("REMOVING EDITOR")

        self.message.setText("This program only removes the Make Python Editor."
                             " To remove Python itself, follow your OS-specific"
                             " uninstallation process")
        self.message.setVisible(1)


        # First, check that it's even instaled in the first place!

        mp_dir = utilities.get_makepython_dir()

        if mp_dir is not None:

            # start uninstaller
            uninstaller = editor_installer.install(self)
            uninstaller.uninstall(mp_dir)


        else:
            self.installbutton.setText("ERROR REMOVING")
            self.message.setText("Could not find Make Python Editor...")
            self.message.setVisible(1)


    def make(self):
        """ start the install OR end the install"""

        self.install_starttime = time()
        if self.progressbar.value() != 100:

            self.installbutton.setText("INSTALLING")

            self.progress_timer = QtCore.QTimer()
            self.progress_timer.timeout.connect(lambda: self.check_progress())
            self.progress_timer.start(2000)
        else:
            print("LAUNCH")
            self.editor_installer.launch_after_install()
            self.progress_timer.stop()
            self.close()

    def check_progress(self):
        """Check installation progress, and update phases"""

        if self.phase_process('core'):
            if self.phase_process('editor'):
                print('--DONE--TOOK:',(time()-self.install_starttime)/60,'min')

        self.update_progress()

    def phase_process(self, phase):
        """ Evaluate which phase we are in, and do that phase's functions  """

        if self.phases[phase]==0:  # start phase
            self.phases[phase]=10
            self.phase_starter[phase]()
            return 0

        elif self.phases[phase] < 100:  # installing phase
            self.phases[phase] = self.phase_handlers[phase].progress()
            return 0

        elif self.phases[phase]==100:  # done phase
            return 1

    def core_install(self):
        """Install the core python"""
        self.core_installer = platform_installer.install(version.V, version.R,
                                                         self)
        self.phase_handlers['core'] = self.core_installer

    def editor_install(self):
        """Install the makepython editor"""
        self.editor_installer = editor_installer.install(self)
        self.phase_handlers['editor'] = self.editor_installer

    def update_progress(self):
        """ update the progress bar! """

        total_percent  = sum(self.phases.values())
        total_percent /= len(self.phases.values())

        if total_percent >= 100:
            self.installbutton.setText("LAUNCH")
            total_percent = 100

        self.progressbar.setValue(total_percent)
        print('%:',total_percent,self.phases.items())

    def mousePressEvent(self, event):
        """Note position so we can drag window"""
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        """Drag window"""
        x=event.globalX()
        y=event.globalY()
        try:
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.move(x-x_w, y-y_w)
        except AttributeError: # don't drag non-whitespace
            pass

    def new_color(self):
        """New background color"""
        r = 127*(sin((time()-self.color_stime)/6-pi/2)+1)
        g = 127*(sin((time()-self.color_stime)/4-pi/2)+1)
        b = 127*(sin((time()-self.color_stime)/2-pi/2)+1)

        rgbs = ''.join(['(', str(r), ',',
                             str(g), ',',
                             str(b), ')'])

        utilities.changeCSS(self.bg,'background','rgb'+rgbs)

def add_to_log(farg, *args):

    x = ''.join([str(farg)+' '] + [ str(arg)+' ' for arg in args ])

    with open('INSTALL.log','a') as f:
        f.write(' ' + str(x) + '\n')

print = add_to_log

def run_installer():

    try:
        print('starting app...')
        app = QtWidgets.QApplication(sys.argv)

        # COMMENT THE NEXT TWO LINES IF TESTING AS A .PY FILE
        QtGui.QFontDatabase.addApplicationFont(sys._MEIPASS+'/fonts/DaisyScript.ttf')
        QtGui.QFontDatabase.addApplicationFont(sys._MEIPASS+'/fonts/LemonMilklight.otf')

        gui  = Interface()
        gui.show()
        app.exec_()

        if install_globals.delete_log_after:
            os.remove('INSTALL.log')  # if all succeeded

    except Exception as e:
        print(e)


if __name__=='__main__':

    if platform.system() == 'Windows':

        if is_admin():
            run_installer()

        else:

            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas",
                                                sys.executable, sys.argv[0],
                                                None,
                                                1) # show new window
    else:

        print('Yo yo! UNIX NOT YET SUPPORTED! :/')
