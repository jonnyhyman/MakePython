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
from math import sin, pi
from time import time
from subprocess import Popen, call
import utilities
import platform
import defaults
import styles
import pipwin
import ctypes # make icon show up on windows
import sys
import os

class PipBar(QtWidgets.QDialog, pipwin.Ui_pip):

    def __init__(self,parent=None,color_mode=1):

        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.color_mode = color_mode

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.unix_close.clicked.connect(self.close)
        self.win_close.clicked.connect(self.close)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Escape"),self)
        self.shortcut.activated.connect(self.close)

        self.plainTextEdit.textChanged.connect(self.textChanged)

        self.system = platform.system()

        self.color_timer = QtCore.QTimer()
        self.color_start = (0,0,0)
        self.color_stime = time()
        self.color_timer.timeout.connect(self.new_color)
        self.color_timer.start(50)

        if self.system == 'Windows':
            self.unix_close.setVisible(0)
            self.win_close.setVisible(1)
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('make')
        else:
            self.unix_close.setVisible(1)
            self.win_close.setVisible(0)

        self.show()

    def textChanged(self):
        """ if we tried to make a newline, override with install """
        text = self.plainTextEdit.toPlainText()

        if len(text) > 0:
            if text[-1] == '\n':
                cursor = self.plainTextEdit.textCursor()
                self.package_name = self.plainTextEdit.toPlainText()[:-1]
                self.plainTextEdit.setPlainText(self.package_name)
                self.plainTextEdit.setTextCursor(cursor)

                self.install()


    def install(self):
        """ open a console, running pip install <package_name> """

        if self.package_name != '':
            if defaults.fork_pip:
                if self.system == 'Windows':
                    os.system('start cmd /K pip install '+self.package_name)
                else:
                    Popen('pip install '+self.package_name, shell=True)
            else:
                call('pip install '+self.package_name, shell=True)
                self.close()

    def mousePressEvent(self, event):
        "Note position so we can drag window"
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        "Drag window"
        x=event.globalX()
        y=event.globalY()
        try:
            x_w = self.offset.x()
            y_w = self.offset.y()
            self.move(x-x_w, y-y_w)
        except AttributeError: # don't drag non-whitespace
            pass

    def new_color(self):
        "New background color"

        r = 127*(sin((time()-self.color_stime)/6-pi/2)+1)
        g = 127*(sin((time()-self.color_stime)/4-pi/2)+1)
        b = 127*(sin((time()-self.color_stime)/2-pi/2)+1)

        rgbas = ''.join(['(', str(r), ',',
                             str(g), ',',
                             str(b), ',',
                             str(styles.ui_colors[self.color_mode]['bg_pip_a']),
                        ')'])

        utilities.changeCSS(self.bg,'background','rgba'+rgbas)

if __name__=='__main__':

    app = QtWidgets.QApplication(sys.argv)
    gui  = Interface()
    gui.show()
    app.exec_()
