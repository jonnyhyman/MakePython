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

"""    ---------------------- HELLO FRIEND! ----------------------

        Welcome to the makepython installer!

        Things go like this, basically:
            - Force installer to run in as an ADMINISTRATOR
            - Detect the OS we're running on (Windows? Mac? Linux?)

            - Install Python ("platform_installer")
            - Install MakePython Editor ("editor_installer")
            - Create shortcuts, path definitions and context menu items


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
    ''' Is the user running the app as admin? -- Windows only'''

    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class Interface(QtWidgets.QMainWindow, installer.Ui_Install):

    """ Interface runs the pretty colors (GUI) and the installation process """

    def __init__(self,parent=None):

        super(self.__class__, self).__init__()  # super initialize from parents

        # this function defines and starts the user interface
        self.setupUi(self)  # run the installer.Ui_Install.setupUi function

        self.message.setVisible(0)  # make error message invisible
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # hide window frame
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # hide background
        self.installbutton.pressed.connect(self.buttonpress) # detect press
        self.installbutton.released.connect(self.buttonrelease) # detect release
        self.unix_close.clicked.connect(self.close) # connect left side X button
        self.win_close.clicked.connect(self.close) # connect right side X button

        self.system = platform.system()  # detect our operating system

        self.color_timer = QtCore.QTimer()  # define a timer
        self.color_start = (0,0,0)  # define the start color
        self.color_stime = time()  # take the start time
        self.color_timer.timeout.connect(self.new_color)  # run @ timeout
        self.color_timer.start(50)  # define the timeout interval (millisec)

        self.progressbar.setValue(0)  # set the progressbar to zero
        self.uninstall = False        # initialize uninstall flag to false

        if self.system == 'Windows':  # hello, mr. and ms. Gates
            self.unix_close.setVisible(0)  # hide the left hand side X
            self.win_close.setVisible(1)   # show the right hand side X

            # The below ugly duckling function makes OS icon visible
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('make')

        else:

            self.unix_close.setVisible(1)  # show the left hand side X
            self.win_close.setVisible(0)   # hide the right hand side X

        # --------------------------------------- Definition of install phases

        # phases variable defines the percentage of installation completion
        # if core is done, will be {'core':100, 'editor':0}
        # if all are done, will be {'core':100, 'editor':100}
        self.phases = {
                        'core'  : 0,  # install python core
                        'editor': 0,  # install python editor
                      }

        # phase_handlers holds the functions to call to check how far the
        # installation has gone so far.

        # We start them as None because we still want to decide which one to
        # use (based on our operating system).

        self.phase_handlers = {
                        'core'  : None,
                        'editor': None,
                        }

        # phase_starter holds the functions to call to actually -start- each
        # phase of the installation process

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

        # if y'all held the install button for more than 5 secs, uninstall!

        if self.held_time <= 5:
            self.make()
        else:
            self.unmake()

    def sendmessage(self,msg):
        """ send a message to the user in the QLabel called self.message """

        self.message.setText(msg)
        self.message.setVisible(1)

    def unmake(self):
        """ uninstall the editor """

        self.uninstall = True
        self.installbutton.setText("REMOVING EDITOR")

        self.sendmessage("This program only removes the Make Python Editor."
                         " To remove Python itself, follow your OS-specific"
                         " uninstallation process")

        # First, check that it's even installed in the first place!

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
        self.core_installer = platform_installer.install(install_globals.V,
                                                         install_globals.R,
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
