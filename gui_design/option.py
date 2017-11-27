# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'option.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Option(object):
    def setupUi(self, Option):
        Option.setObjectName("Option")
        Option.resize(250, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Option.sizePolicy().hasHeightForWidth())
        Option.setSizePolicy(sizePolicy)
        Option.setMinimumSize(QtCore.QSize(250, 100))
        Option.setMaximumSize(QtCore.QSize(250, 100))
        Option.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Option.setWindowIcon(icon)
        Option.setStatusTip("")
        Option.setStyleSheet("")
        self.bg = QtWidgets.QLabel(Option)
        self.bg.setEnabled(True)
        self.bg.setGeometry(QtCore.QRect(0, 0, 249, 100))
        self.bg.setStyleSheet("background:rgb(0,0,0);\n"
"border:0px solid black;\n"
"border-radius: 20%;")
        self.bg.setText("")
        self.bg.setAlignment(QtCore.Qt.AlignCenter)
        self.bg.setObjectName("bg")
        self.unix_close = QtWidgets.QPushButton(Option)
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
        self.gridLayoutWidget = QtWidgets.QWidget(Option)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 0, 187, 103))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.left = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.left.setMinimumSize(QtCore.QSize(40, 40))
        self.left.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.left.setFont(font)
        self.left.setToolTipDuration(-1)
        self.left.setStatusTip("")
        self.left.setWhatsThis("")
        self.left.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #0023a4;\n"
"    border: 0px solid white;\n"
"    border-radius:20px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #0C75E8;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border: 2px solid #94ff94;\n"
"    background-color: #0d242e;\n"
"}")
        self.left.setObjectName("left")
        self.gridLayout.addWidget(self.left, 0, 0, 1, 1)
        self.right = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.right.setMinimumSize(QtCore.QSize(40, 40))
        self.right.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.right.setFont(font)
        self.right.setToolTipDuration(-1)
        self.right.setStatusTip("")
        self.right.setWhatsThis("")
        self.right.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #0023a4;\n"
"    border: 0px solid white;\n"
"    border-radius:20px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #0C75E8;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    border: 2px solid #94ff94;\n"
"    background-color: #0d242e;\n"
"}")
        self.right.setObjectName("right")
        self.gridLayout.addWidget(self.right, 0, 1, 1, 1)
        self.win_close = QtWidgets.QPushButton(Option)
        self.win_close.setGeometry(QtCore.QRect(210, 4, 33, 33))
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

        self.retranslateUi(Option)
        QtCore.QMetaObject.connectSlotsByName(Option)

    def retranslateUi(self, Option):
        _translate = QtCore.QCoreApplication.translate
        Option.setWindowTitle(_translate("Option", "Option"))
        self.unix_close.setText(_translate("Option", "x"))
        self.left.setToolTip(_translate("Option", "New | Ctrl + N"))
        self.left.setText(_translate("Option", "LEFT"))
        self.right.setToolTip(_translate("Option", "New | Ctrl + N"))
        self.right.setText(_translate("Option", "RIGHT"))
        self.win_close.setText(_translate("Option", "x"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Option = QtWidgets.QDialog()
    ui = Ui_Option()
    ui.setupUi(Option)
    Option.show()
    sys.exit(app.exec_())

