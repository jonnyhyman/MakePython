# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(848, 706)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Editor.sizePolicy().hasHeightForWidth())
        Editor.setSizePolicy(sizePolicy)
        Editor.setMinimumSize(QtCore.QSize(0, 0))
        Editor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Fira Mono")
        font.setPointSize(10)
        Editor.setFont(font)
        Editor.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Editor.setWindowIcon(icon)
        Editor.setStatusTip("")
        Editor.setAutoFillBackground(False)
        Editor.setStyleSheet("background: #f0f0f0;")
        self.centralWidget = QtWidgets.QWidget(Editor)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.findandreplace_closebutton = QtWidgets.QPushButton(self.centralWidget)
        self.findandreplace_closebutton.setMinimumSize(QtCore.QSize(25, 25))
        self.findandreplace_closebutton.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(7)
        font.setItalic(False)
        self.findandreplace_closebutton.setFont(font)
        self.findandreplace_closebutton.setToolTipDuration(-1)
        self.findandreplace_closebutton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #0023a4;\n"
"    border: 0px solid white;\n"
"    border-radius:12px;\n"
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
        self.findandreplace_closebutton.setObjectName("findandreplace_closebutton")
        self.horizontalLayout.addWidget(self.findandreplace_closebutton)
        self.findText = QtWidgets.QPlainTextEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.findText.sizePolicy().hasHeightForWidth())
        self.findText.setSizePolicy(sizePolicy)
        self.findText.setMinimumSize(QtCore.QSize(0, 27))
        self.findText.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.findText.setFont(font)
        self.findText.setStyleSheet("QPlainTextEdit{\n"
"    color: black;\n"
"    background: white;\n"
"    border: 0px solid #0023a4;\n"
"    border-radius: 5px;\n"
"}")
        self.findText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.findText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.findText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.findText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.findText.setTabChangesFocus(True)
        self.findText.setUndoRedoEnabled(False)
        self.findText.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.findText.setCenterOnScroll(True)
        self.findText.setObjectName("findText")
        self.horizontalLayout.addWidget(self.findText)
        self.replaceText = QtWidgets.QPlainTextEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.replaceText.sizePolicy().hasHeightForWidth())
        self.replaceText.setSizePolicy(sizePolicy)
        self.replaceText.setMinimumSize(QtCore.QSize(0, 27))
        self.replaceText.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.replaceText.setFont(font)
        self.replaceText.setStyleSheet("QPlainTextEdit{\n"
"    color: black;\n"
"    background: white;\n"
"    border: 0px solid #0023a4;\n"
"    border-radius: 5px;\n"
"}")
        self.replaceText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.replaceText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.replaceText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.replaceText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.replaceText.setTabChangesFocus(True)
        self.replaceText.setUndoRedoEnabled(False)
        self.replaceText.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.replaceText.setCenterOnScroll(True)
        self.replaceText.setObjectName("replaceText")
        self.horizontalLayout.addWidget(self.replaceText)
        self.findandreplace_findbutton = QtWidgets.QPushButton(self.centralWidget)
        self.findandreplace_findbutton.setMinimumSize(QtCore.QSize(25, 25))
        self.findandreplace_findbutton.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(6)
        font.setItalic(False)
        self.findandreplace_findbutton.setFont(font)
        self.findandreplace_findbutton.setToolTipDuration(-1)
        self.findandreplace_findbutton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #0023a4;\n"
"    border: 0px solid white;\n"
"    border-radius:12px;\n"
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
        self.findandreplace_findbutton.setObjectName("findandreplace_findbutton")
        self.horizontalLayout.addWidget(self.findandreplace_findbutton)
        self.findandreplace_replacebutton = QtWidgets.QPushButton(self.centralWidget)
        self.findandreplace_replacebutton.setMinimumSize(QtCore.QSize(25, 25))
        self.findandreplace_replacebutton.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setItalic(False)
        self.findandreplace_replacebutton.setFont(font)
        self.findandreplace_replacebutton.setToolTipDuration(-1)
        self.findandreplace_replacebutton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background-color: #0023a4;\n"
"    border: 0px solid white;\n"
"    border-radius:12px;\n"
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
        self.findandreplace_replacebutton.setObjectName("findandreplace_replacebutton")
        self.horizontalLayout.addWidget(self.findandreplace_replacebutton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Fira Mono")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    color: black;\n"
"    font: 10pt Fira Mono;\n"
"    background: white;\n"
"    border: 0px solid #0023a4;\n"
"    border-radius: 5px;\n"
"    padding: 5%;\n"
"}\n"
"QScrollBar::vertical {\n"
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
"QScrollBar::horizontal {\n"
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
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 2px solid grey;\n"
"    background: #32CC99;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 2, 2, 1, 1)
        self.messageText = QtWidgets.QTextEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageText.sizePolicy().hasHeightForWidth())
        self.messageText.setSizePolicy(sizePolicy)
        self.messageText.setMinimumSize(QtCore.QSize(0, 0))
        self.messageText.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setFamily("Fira Mono")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.messageText.setFont(font)
        self.messageText.setStyleSheet("QTextEdit{\n"
"    color: black;\n"
"    font: 7pt Fira Mono;\n"
"    background: white;\n"
"    border: 0px solid #0023a4;\n"
"    border-radius: 5px;\n"
"    padding: 2%;\n"
"}")
        self.messageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.messageText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.messageText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messageText.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messageText.setUndoRedoEnabled(False)
        self.messageText.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.messageText.setReadOnly(True)
        self.messageText.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.messageText.setObjectName("messageText")
        self.gridLayout_2.addWidget(self.messageText, 3, 2, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setMinimumSize(QtCore.QSize(100, 0))
        self.widget.setToolTipDuration(-1)
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(4, 4, 92, 569))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pybutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pybutton.setMinimumSize(QtCore.QSize(90, 90))
        self.pybutton.setMaximumSize(QtCore.QSize(90, 90))
        font = QtGui.QFont()
        font.setFamily("Daisy Script")
        font.setPointSize(48)
        font.setItalic(False)
        self.pybutton.setFont(font)
        self.pybutton.setToolTipDuration(-1)
        self.pybutton.setStyleSheet("QPushButton{\n"
"    color: #0023a4;\n"
"    background: transparent;\n"
"    border: 0px solid white;\n"
"    border-radius:45px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    border: 2px solid #94ff94;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    color:white;\n"
"    border: 2px solid #94ff94;\n"
"    background-color: #0d242e;\n"
"}")
        self.pybutton.setObjectName("pybutton")
        self.verticalLayout.addWidget(self.pybutton)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sourcebutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sourcebutton.setMinimumSize(QtCore.QSize(40, 40))
        self.sourcebutton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setItalic(False)
        self.sourcebutton.setFont(font)
        self.sourcebutton.setToolTipDuration(-1)
        self.sourcebutton.setStyleSheet("QPushButton{\n"
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
        self.sourcebutton.setObjectName("sourcebutton")
        self.gridLayout.addWidget(self.sourcebutton, 5, 0, 1, 1)
        self.findbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.findbutton.setMinimumSize(QtCore.QSize(40, 40))
        self.findbutton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setItalic(False)
        self.findbutton.setFont(font)
        self.findbutton.setToolTipDuration(-1)
        self.findbutton.setStyleSheet("QPushButton{\n"
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
        self.findbutton.setObjectName("findbutton")
        self.gridLayout.addWidget(self.findbutton, 4, 0, 1, 1)
        self.openbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.openbutton.setMinimumSize(QtCore.QSize(40, 40))
        self.openbutton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.openbutton.setFont(font)
        self.openbutton.setToolTipDuration(-1)
        self.openbutton.setStyleSheet("QPushButton{\n"
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
        self.openbutton.setObjectName("openbutton")
        self.gridLayout.addWidget(self.openbutton, 1, 0, 1, 1)
        self.savebutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.savebutton.setMinimumSize(QtCore.QSize(40, 40))
        self.savebutton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.savebutton.setFont(font)
        self.savebutton.setToolTipDuration(-1)
        self.savebutton.setStyleSheet("QPushButton{\n"
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
        self.savebutton.setObjectName("savebutton")
        self.gridLayout.addWidget(self.savebutton, 2, 0, 1, 1)
        self.newbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.newbutton.setMinimumSize(QtCore.QSize(40, 40))
        self.newbutton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.newbutton.setFont(font)
        self.newbutton.setToolTipDuration(-1)
        self.newbutton.setStatusTip("")
        self.newbutton.setWhatsThis("")
        self.newbutton.setStyleSheet("QPushButton{\n"
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
        self.newbutton.setObjectName("newbutton")
        self.gridLayout.addWidget(self.newbutton, 0, 0, 1, 1)
        self.shellbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.shellbutton.setMinimumSize(QtCore.QSize(40, 40))
        self.shellbutton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setItalic(False)
        self.shellbutton.setFont(font)
        self.shellbutton.setToolTipDuration(-1)
        self.shellbutton.setStyleSheet("QPushButton{\n"
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
        self.shellbutton.setObjectName("shellbutton")
        self.gridLayout.addWidget(self.shellbutton, 3, 0, 1, 1)
        self.colorbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.colorbutton.setMinimumSize(QtCore.QSize(40, 40))
        self.colorbutton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setItalic(False)
        self.colorbutton.setFont(font)
        self.colorbutton.setToolTipDuration(-1)
        self.colorbutton.setStyleSheet("QPushButton{\n"
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
        self.colorbutton.setObjectName("colorbutton")
        self.gridLayout.addWidget(self.colorbutton, 7, 0, 1, 1)
        self.pipbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pipbutton.setMinimumSize(QtCore.QSize(40, 40))
        self.pipbutton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        font.setItalic(False)
        self.pipbutton.setFont(font)
        self.pipbutton.setToolTipDuration(-1)
        self.pipbutton.setStyleSheet("QPushButton{\n"
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
        self.pipbutton.setObjectName("pipbutton")
        self.gridLayout.addWidget(self.pipbutton, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 5, 1)
        Editor.setCentralWidget(self.centralWidget)

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("Editor", "Make Python Editor"))
        self.findandreplace_closebutton.setToolTip(_translate("Editor", "Close Find & Replace | Escape"))
        self.findandreplace_closebutton.setText(_translate("Editor", "X"))
        self.findText.setPlaceholderText(_translate("Editor", "Type text to find"))
        self.replaceText.setPlaceholderText(_translate("Editor", "Type replacement text"))
        self.findandreplace_findbutton.setToolTip(_translate("Editor", "Find | Highlight Text to Find + Enter"))
        self.findandreplace_findbutton.setText(_translate("Editor", "🔎"))
        self.findandreplace_replacebutton.setToolTip(_translate("Editor", "Replace | Highlight Replacement Text + Enter"))
        self.findandreplace_replacebutton.setText(_translate("Editor", "⇋"))
        self.textEdit.setHtml(_translate("Editor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Fira Mono\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.messageText.setHtml(_translate("Editor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Fira Mono\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is an error message</p></body></html>"))
        self.pybutton.setToolTip(_translate("Editor", "Launch | Ctrl + Enter"))
        self.pybutton.setText(_translate("Editor", "py"))
        self.sourcebutton.setToolTip(_translate("Editor", "Open Module Source | Ctrl + M"))
        self.sourcebutton.setText(_translate("Editor", "👁"))
        self.findbutton.setToolTip(_translate("Editor", "Find | Ctrl + F"))
        self.findbutton.setText(_translate("Editor", "🔎"))
        self.openbutton.setToolTip(_translate("Editor", "Open | Ctrl + O"))
        self.openbutton.setText(_translate("Editor", "📤"))
        self.savebutton.setToolTip(_translate("Editor", "Save | Ctrl + S"))
        self.savebutton.setText(_translate("Editor", "📥"))
        self.newbutton.setToolTip(_translate("Editor", "New | Ctrl + N"))
        self.newbutton.setText(_translate("Editor", "+"))
        self.shellbutton.setToolTip(_translate("Editor", "Python Shell | Ctrl + Shift + Enter"))
        self.shellbutton.setText(_translate("Editor", ">>"))
        self.colorbutton.setToolTip(_translate("Editor", "Light / Dark | Ctrl + B"))
        self.colorbutton.setText(_translate("Editor", "☯"))
        self.pipbutton.setToolTip(_translate("Editor", "Package Installer | Ctrl+P"))
        self.pipbutton.setText(_translate("Editor", "📦"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QMainWindow()
    ui = Ui_Editor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())

