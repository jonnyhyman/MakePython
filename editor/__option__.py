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
import option
import ctypes # make icon show up on windows
import sys
import os

class Option(QtWidgets.QDialog, option.Ui_Option):

    def __init__(self, left_right, control_funcs, ui):

        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.ui = ui

        # 0th element should always correspond to cancel
        self.functions = control_funcs

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.unix_close.clicked.connect(self.cancel)
        self.win_close.clicked.connect(self.cancel)

        self.left.setText(left_right[1])
        self.right.setText(left_right[2])

        self.left.clicked.connect(self.returnLeft)
        self.right.clicked.connect(self.returnRight)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Escape"),self)
        self.shortcut.activated.connect(self.close)  # close or cancel?

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

        self.exec_()

    def cancel(self):
        self.functions[0]()
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
                             str(0.8),
                        ')'])

        utilities.changeCSS(self.bg,'background','rgba'+rgbas)

    def returnLeft(self):
        self.functions[0]()
        self.close()
        return 0

    def returnRight(self):
        self.functions[1]()
        self.close()
        return 1

if __name__=='__main__':

    app = QtWidgets.QApplication(sys.argv)
    gui  = Interface()
    gui.show()
    app.exec_()
