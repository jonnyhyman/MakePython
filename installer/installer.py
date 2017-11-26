# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
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

class Ui_Install(object):
    def setupUi(self, Install):
        Install.setObjectName("Install")
        Install.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Install.sizePolicy().hasHeightForWidth())
        Install.setSizePolicy(sizePolicy)
        Install.setMinimumSize(QtCore.QSize(800, 500))
        Install.setMaximumSize(QtCore.QSize(800, 500))
        Install.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Install.setWindowIcon(icon)
        Install.setStatusTip("")
        Install.setStyleSheet("")
        self.bg = QtWidgets.QLabel(Install)
        self.bg.setEnabled(True)
        self.bg.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.bg.setStyleSheet("background:rgb(0,0,0);\n"
"border:0px solid black;\n"
"border-radius: 20%;")
        self.bg.setText("")
        self.bg.setAlignment(QtCore.Qt.AlignCenter)
        self.bg.setObjectName("bg")
        self.verticalLayoutWidget = QtWidgets.QWidget(Install)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(228, 136, 345, 203))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Daisy Script")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.installbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.installbutton.setMinimumSize(QtCore.QSize(343, 56))
        self.installbutton.setMaximumSize(QtCore.QSize(343, 56))
        font = QtGui.QFont()
        font.setFamily("Lemon/Milk light")
        font.setPointSize(20)
        self.installbutton.setFont(font)
        self.installbutton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #0074a4;\n"
"    border: 0px solid #0d242e;\n"
"    border-radius:5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border: 1px solid white;\n"
"    background-color: #0d242e;\n"
"}")
        self.installbutton.setObjectName("installbutton")
        self.verticalLayout.addWidget(self.installbutton)
        self.progressbar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progressbar.setMinimumSize(QtCore.QSize(343, 10))
        self.progressbar.setMaximumSize(QtCore.QSize(343, 10))
        self.progressbar.setStyleSheet("QProgressBar {\n"
"background-color: transparent;\n"
"border: 0px solid white;\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color: white;\n"
"border: 1px solid white;\n"
"border-radius:5px;\n"
"}")
        self.progressbar.setProperty("value", 24)
        self.progressbar.setTextVisible(False)
        self.progressbar.setFormat("")
        self.progressbar.setObjectName("progressbar")
        self.verticalLayout.addWidget(self.progressbar)
        self.win_close = QtWidgets.QPushButton(Install)
        self.win_close.setGeometry(QtCore.QRect(752, 10, 33, 33))
        font = QtGui.QFont()
        font.setFamily("CommercialPi BT")
        font.setPointSize(12)
        self.win_close.setFont(font)
        self.win_close.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 0px solid white;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #1a1a1a;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #353534;\n"
"}")
        self.win_close.setObjectName("win_close")
        self.unix_close = QtWidgets.QPushButton(Install)
        self.unix_close.setGeometry(QtCore.QRect(10, 10, 33, 33))
        font = QtGui.QFont()
        font.setFamily("CommercialPi BT")
        font.setPointSize(12)
        self.unix_close.setFont(font)
        self.unix_close.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: transparent;\n"
"    border: 0px solid white;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #1a1a1a;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    background-color: #353534;\n"
"}")
        self.unix_close.setObjectName("unix_close")
        self.message = QtWidgets.QLabel(Install)
        self.message.setGeometry(QtCore.QRect(54, 6, 687, 57))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.message.setFont(font)
        self.message.setStyleSheet("color:white;")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")

        self.retranslateUi(Install)
        QtCore.QMetaObject.connectSlotsByName(Install)

    def retranslateUi(self, Install):
        _translate = QtCore.QCoreApplication.translate
        Install.setWindowTitle(_translate("Install", "Make Python Installer"))
        self.label.setText(_translate("Install", "makepython"))
        self.installbutton.setText(_translate("Install", "INSTALL"))
        self.win_close.setText(_translate("Install", "x"))
        self.unix_close.setText(_translate("Install", "x"))
        self.message.setText(_translate("Install", "Installation messages can go here!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Install = QtWidgets.QDialog()
    ui = Ui_Install()
    ui.setupUi(Install)
    Install.show()
    sys.exit(app.exec_())
