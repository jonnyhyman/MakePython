# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initwin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_init(object):
    def setupUi(self, init):
        init.setObjectName("init")
        init.resize(600, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(init.sizePolicy().hasHeightForWidth())
        init.setSizePolicy(sizePolicy)
        init.setMinimumSize(QtCore.QSize(600, 100))
        init.setMaximumSize(QtCore.QSize(600, 100))
        init.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        init.setWindowIcon(icon)
        init.setStatusTip("")
        init.setStyleSheet("")
        self.bg = QtWidgets.QLabel(init)
        self.bg.setEnabled(True)
        self.bg.setGeometry(QtCore.QRect(0, 0, 600, 100))
        self.bg.setStyleSheet("background:rgb(0,0,0);\n"
"border:0px solid black;\n"
"border-radius: 20%;")
        self.bg.setText("")
        self.bg.setAlignment(QtCore.Qt.AlignCenter)
        self.bg.setObjectName("bg")
        self.unix_close = QtWidgets.QPushButton(init)
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
        self.gridLayoutWidget = QtWidgets.QWidget(init)
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
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setMaximumBlockCount(2)
        self.plainTextEdit.setCenterOnScroll(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.installTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.installTextEdit.sizePolicy().hasHeightForWidth())
        self.installTextEdit.setSizePolicy(sizePolicy)
        self.installTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.installTextEdit.setFont(font)
        self.installTextEdit.setStyleSheet("color: white;\n"
"background: transparent;\n"
"padding: 7%;")
        self.installTextEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.installTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.installTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.installTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.installTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.installTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.installTextEdit.setReadOnly(True)
        self.installTextEdit.setPlainText("")
        self.installTextEdit.setMaximumBlockCount(2)
        self.installTextEdit.setCenterOnScroll(True)
        self.installTextEdit.setPlaceholderText("")
        self.installTextEdit.setObjectName("installTextEdit")
        self.gridLayout.addWidget(self.installTextEdit, 0, 1, 1, 1)
        self.win_close = QtWidgets.QPushButton(init)
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

        self.retranslateUi(init)
        QtCore.QMetaObject.connectSlotsByName(init)

    def retranslateUi(self, init):
        _translate = QtCore.QCoreApplication.translate
        init.setWindowTitle(_translate("init", "Make Python Starter"))
        self.unix_close.setText(_translate("init", "x"))
        self.plainTextEdit.setPlaceholderText(_translate("init", "Finishing Installation"))
        self.win_close.setText(_translate("init", "x"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    init = QtWidgets.QDialog()
    ui = Ui_init()
    ui.setupUi(init)
    init.show()
    sys.exit(app.exec_())

