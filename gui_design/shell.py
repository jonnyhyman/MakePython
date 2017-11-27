# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shell.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Shell(object):
    def setupUi(self, Shell):
        Shell.setObjectName("Shell")
        Shell.resize(727, 323)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Shell.sizePolicy().hasHeightForWidth())
        Shell.setSizePolicy(sizePolicy)
        Shell.setMinimumSize(QtCore.QSize(0, 0))
        Shell.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Fira Mono")
        font.setPointSize(10)
        Shell.setFont(font)
        Shell.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Shell.setWindowIcon(icon)
        Shell.setStatusTip("")
        Shell.setAutoFillBackground(False)
        Shell.setStyleSheet("background:#f0f0f0;")
        self.centralWidget = QtWidgets.QWidget(Shell)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Monospac821 BT")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    background: white;\n"
"    border: 0px solid #0023a4;\n"
"    padding: 5%;\n"
"}\n"
"QScrollBar:vertical {\n"
"        border: 0px solid white;\n"
"        background:#ebebeb;\n"
"        margin: 0px 0px 0px 0px;\n"
"        width: 10px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #d2d2d2;\n"
"    border: 0px solid black;\n"
"    border-radius: 5px;\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"        border: 0px solid white;\n"
"        background:#ebebeb;\n"
"        margin: 0px 0px 0px 0px;\n"
"        height: 10px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #d2d2d2;\n"
"    border: 0px solid black;\n"
"    border-radius: 5px;\n"
"    min-width: 0px;\n"
"}")
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        Shell.setCentralWidget(self.centralWidget)

        self.retranslateUi(Shell)
        QtCore.QMetaObject.connectSlotsByName(Shell)

    def retranslateUi(self, Shell):
        _translate = QtCore.QCoreApplication.translate
        Shell.setWindowTitle(_translate("Shell", "Python Shell"))
        self.textEdit.setHtml(_translate("Shell", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospac821 BT\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Shell = QtWidgets.QMainWindow()
    ui = Ui_Shell()
    ui.setupUi(Shell)
    Shell.show()
    sys.exit(app.exec_())

