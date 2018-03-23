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
from gui_designs import initwin
from subprocess import Popen
from math import sin, pi
from time import time
import platform
import ctypes

def extractCSS(style,att):
    beg   = style.index(att)+len(att)+1 # don't include :
    end   = style.index(';',beg) # don't include ';'
    return style[beg:end]

def changeCSS(obj,attribute,target):
    style = obj.styleSheet()
    style = style.replace(extractCSS(style,attribute),target)
    obj.setStyleSheet(style)

class InitWin(QtWidgets.QDialog, initwin.Ui_init):

    def __init__(self,install_message,process_args,parent=None):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.installTextEdit.setPlainText(install_message)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.unix_close.clicked.connect(self.close)
        self.win_close.clicked.connect(self.close)
        self.system = platform.system()

        if self.system == 'Windows':
            self.unix_close.setVisible(0)
            self.win_close.setVisible(1)
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('make')
        else:
            self.unix_close.setVisible(1)
            self.win_close.setVisible(0)

        self.upd_timer = QtCore.QTimer()
        self.color_start = (0,0,0)
        self.color_stime = time()
        self.upd_timer.timeout.connect(self.update)
        self.upd_timer.start(50)

        self.prc = Popen(process_args, shell=True)  # forward shell to current process

        self.show()

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

    def update(self):
        "New background color"

        r = 127*(sin((time()-self.color_stime)/6-pi/2)+1)
        g = 127*(sin((time()-self.color_stime)/4-pi/2)+1)
        b = 127*(sin((time()-self.color_stime)/2-pi/2)+1)

        rgbas = ''.join(['(', str(r), ',',
                             str(g), ',',
                             str(b), ',',
                             str(0.8),')'])

        changeCSS(self.bg,'background','rgba'+rgbas)

        if self.prc.poll() is not None:
            self.upd_timer.stop()
            self.close()

if __name__=='__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    gui = InitWin('installing some dope stuff',['pip','install','nose'])
    gui.show()
    app.exec_()
