# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pipwin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pip(object):
    def setupUi(self, pip):
        pip.setObjectName("pip")
        pip.resize(600, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pip.sizePolicy().hasHeightForWidth())
        pip.setSizePolicy(sizePolicy)
        pip.setMinimumSize(QtCore.QSize(600, 100))
        pip.setMaximumSize(QtCore.QSize(600, 100))
        pip.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pip.setWindowIcon(icon)
        pip.setStatusTip("")
        pip.setStyleSheet("")
        self.bg = QtWidgets.QLabel(pip)
        self.bg.setEnabled(True)
        self.bg.setGeometry(QtCore.QRect(0, 0, 600, 100))
        self.bg.setStyleSheet("background:rgb(0,0,0);\n"
"border:0px solid black;\n"
"border-radius: 20%;")
        self.bg.setText("")
        self.bg.setAlignment(QtCore.Qt.AlignCenter)
        self.bg.setObjectName("bg")
        self.unix_close = QtWidgets.QPushButton(pip)
        self.unix_close.setGeometry(QtCore.QRect(6, 6, 33, 33))
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
        self.gridLayoutWidget = QtWidgets.QWidget(pip)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 24, 521, 57))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color: white;\n"
"background: transparent;\n"
"padding: 7%;")
        self.plainTextEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit.setMaximumBlockCount(2)
        self.plainTextEdit.setCenterOnScroll(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.win_close = QtWidgets.QPushButton(pip)
        self.win_close.setGeometry(QtCore.QRect(562, 6, 33, 33))
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
        self.bg.raise_()
        self.gridLayoutWidget.raise_()
        self.unix_close.raise_()
        self.win_close.raise_()

        self.retranslateUi(pip)
        QtCore.QMetaObject.connectSlotsByName(pip)

    def retranslateUi(self, pip):
        _translate = QtCore.QCoreApplication.translate
        pip.setWindowTitle(_translate("pip", "Python Package Installer"))
        self.unix_close.setText(_translate("pip", "x"))
        self.plainTextEdit.setPlaceholderText(_translate("pip", "Type PyPI Package Name + Press Enter"))
        self.win_close.setText(_translate("pip", "x"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pip = QtWidgets.QDialog()
    ui = Ui_pip()
    ui.setupUi(pip)
    pip.show()
    sys.exit(app.exec_())

