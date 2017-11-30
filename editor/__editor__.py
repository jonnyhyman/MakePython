'''---------------------------------------------------------------------------
Copyright (C) 2017, Jonathan "Jonny" Hyman
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
---------------------------------------------------------------------------
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from subprocess import Popen
from platform import system
import utilities as utils
import __option__ as opt
import __pipwin__ as pip
import importlib.util
import defaults
import inspect
import ctypes # make icon show up on windows
import styles
import syntax
import editor
import sys
import os

class ActionWatcher(QtCore.QObject):
    def __init__(self,parent=None):
        """ This class is solely for intercepting events """
        QtCore.QObject.__init__(self)
        self.parent = parent

    def eventFilter(self,obj,event):
        ''' Watch for events and emit if they have actions associated '''

        if (obj == self.parent.textEdit and event.type() == QtCore.QEvent.Wheel ):
            if event.modifiers() == QtCore.Qt.ControlModifier:
                if (event.angleDelta().y() > 0):
                    self.parent.changeFontSize(+1)
                else:
                    self.parent.changeFontSize(-1)
                return 1

        if (obj == self.parent.textEdit and event.type() == QtCore.QEvent.KeyPress ):

            # if we don't clear brace highlights every keypress,
            # BEFORE the textEdit is allowed to update
            # the highlighted brace's in-block-positions will be erroneous
            # because of the changed text in textEdit

            self.parent.highlighter.clearBraceHighlights()

            if event.key() in [QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter]:
                self.parent.indentationMatch()
                return 1

            # Currently deprecated due to newline eating problem - see Issues

            if event.key() in [QtCore.Qt.Key_Tab, QtCore.Qt.Key_Backtab]:
                if event.modifiers() == QtCore.Qt.ShiftModifier:
                    self.parent.deIndent()
                    return 1
                else:
                    self.parent.indent()
                    return 1

            if event.key() == QtCore.Qt.Key_BracketLeft:
                if event.modifiers() == QtCore.Qt.ControlModifier:
                    self.parent.deIndent()
                    return 1

            if event.key() == QtCore.Qt.Key_BracketRight:
                if event.modifiers() == QtCore.Qt.ControlModifier:
                    self.parent.indent()
                    return 1

            if event.key() in [QtCore.Qt.Key_ParenLeft,   # ()
                               QtCore.Qt.Key_BracketLeft, # []
                               QtCore.Qt.Key_BraceLeft]:  # {}
                self.parent.braceHelper(event.key())
                return 1


        return self.parent.eventFilter(obj,event)

class Interface(QtWidgets.QMainWindow, editor.Ui_Editor):

    undo = []
    redo = []

    def __init__(self, parent=None):
        """ This class houses the entire editor interface, including
            most functions related to text editing
        """

        # initialize the editor
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.root = os.path.realpath(__file__)  # where to find defaults.py and assets
        self.root = os.path.dirname(self.root)
        self.root+= '\\'

        for font in os.listdir( self.root + 'fonts' ):
            QtGui.QFontDatabase.addApplicationFont(self.root + 'fonts\\' + font)
            print('font initted:',font)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.root+"icon.png"),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)

        self.setWindowIcon(icon)

        self.color_mode = defaults.color_mode

        self.system = system()  # from platform module
        if self.system == 'Windows':
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('edit')

        # set up the editor style
        self.fontsize = defaults.font_size
        self.highlighter = syntax.PythonHighlighter(self.textEdit,
                                                    self.color_mode)

        self.actionSetup()
        self.buttonSetup()
        self.closeFind()
        self.flipTheme(override=True)
        self.messageText.setVisible(0)

        # set up properties of this specific python script
        if len(sys.argv) == 1:
            self.file = ''
        else:
            self.file = sys.argv[1]
            self.open(no_dialog=True)

        self.setWindowTitle(self.windowTitle()+'*')
        self.textEdit.textChanged.connect(self.textChange)
        self.textEdit.cursorPositionChanged.connect(self.textCursorChange)

        self.findText.textChanged.connect(self.findTextChange)
        self.replaceText.textChanged.connect(self.replaceTextChange)

        self.setupFont()
        self.captureHistory()  # prime the undo buffer
        self.textEdit.setFocus()

    def actionSetup(self):
        """ tie in keyboard actions and button presses """
        self.actionFilter = ActionWatcher(self)
        self.textEdit.installEventFilter(self.actionFilter)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence.ZoomIn,self)
        self.shortcut.activated.connect(lambda: self.changeFontSize(+1))

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+="),self)
        self.shortcut.activated.connect(lambda: self.changeFontSize(+1))

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence.ZoomOut,self)
        self.shortcut.activated.connect(lambda: self.changeFontSize(-1))

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence.New,self)
        self.shortcut.activated.connect(self.new)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence.Open,self)
        self.shortcut.activated.connect(self.open)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence.Save,self)
        self.shortcut.activated.connect(self.save)

        self.shortcut = QtWidgets.QShortcut(QtCore.Qt.Key_F5,self)
        self.shortcut.activated.connect(self.launch)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Return"),self)
        self.shortcut.activated.connect(self.launch)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Shift+Return"),self)
        self.shortcut.activated.connect(self.newShell)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+f"),self)
        self.shortcut.activated.connect(self.find)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Escape"),self)
        self.shortcut.activated.connect(self.closeFindShortcut)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+b"),self)
        self.shortcut.activated.connect(self.flipTheme)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+m"),self)
        self.shortcut.activated.connect(self.findSource)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+p"),self)
        self.shortcut.activated.connect(self.openPIP)

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Up"),self)
        self.shortcut.activated.connect(lambda: self.blockMove(+1))

        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Down"),self)
        self.shortcut.activated.connect(lambda: self.blockMove(-1))

    def buttonSetup(self):
        """ connect buttons """

        self.buttons = [
                        self.newbutton,
                        self.pipbutton,
                        self.openbutton,
                        self.savebutton,
                        self.shellbutton,
                        self.findbutton,
                        self.sourcebutton,
                        self.colorbutton,
                        self.findandreplace_closebutton,
                        self.findandreplace_findbutton,
                        self.findandreplace_replacebutton,
                        ]

        self.newbutton.clicked.connect(self.new)
        self.pybutton.clicked.connect(self.launch)
        self.openbutton.clicked.connect(self.open)
        self.savebutton.clicked.connect(self.save)
        self.pipbutton.clicked.connect(self.openPIP)
        self.shellbutton.clicked.connect(self.newShell)
        self.sourcebutton.clicked.connect(self.findSource)
        self.findandreplace_closebutton.clicked.connect(self.closeFind)
        self.findandreplace_replacebutton.clicked.connect(lambda: self.replaceTextChange(force=True))
        self.findandreplace_findbutton.clicked.connect(lambda: self.findTextChange(force=True))
        self.colorbutton.clicked.connect(self.flipTheme)
        self.findbutton.clicked.connect(self.find)

    def captureHistory(self):
        """ capture current text state, and cursor state """

        text = self.textEdit.toPlainText()
        curs = self.textEdit.textCursor().position()

        if len(self.undo)==0 or text != self.undo[-1][0]:
            self.undo.append([text, curs])

            if len(self.undo) >= defaults.undo_size:
                self.undo.pop(0)

    def textChange(self):
        """ actions upon change of text """

        self.captureHistory()

        if self.file != '':
            # check for diffs
            with open(self.file,'r',encoding='utf-8') as f:
                saved_text = f.read()

            saved_text = saved_text.replace('    ','\t')  # indent consistency

            if saved_text != self.textEdit.toPlainText():
                self.saveState(0)
            else:
                self.saveState(1)

    def indentationMatch(self):
        """ match indentation upon newline """

        cursor = self.textEdit.textCursor()

        indentation = cursor.block().text()
        indentation = ''.join( ['\t' for c in indentation if c == '\t'] )
        indentation = '\n'+indentation
        cursor.insertText(indentation)

    def dent(self,de=False):
        """ perform an indent or deindent operation """

        cursor = self.textEdit.textCursor()

        if not cursor.hasSelection():
            # single line dentation

            cursor.select(QtGui.QTextCursor.BlockUnderCursor)

            # QString --> utf-8
            selected = cursor.selectedText().replace(u"\u2029",'\n')

            if de:  # DETABBING
                if len(selected) > 0:  # if line has some length
                    if selected[0] == '\t':  # if b'\tblock'
                        new_kid_on_the_block = selected[1:] # del 0th '\t'

                    elif selected[0:2] == '\n\t':  # if b'\n\tblock'
                        new_kid_on_the_block = '\n'+selected[2:] # do '\nblock'

                    else:  # not 0th = '\t' AND not '\n\t'
                        new_kid_on_the_block = selected

                else:
                    new_kid_on_the_block = selected

            else:  # NOT DETABBING
                if len(selected) > 0 and selected[0] == '\n':
                    new_kid_on_the_block = '\n' + '\t' + selected[1:]
                else:  # if clean line OR 0th not '\n'
                    new_kid_on_the_block = '\t' + selected

            cursor.insertText(new_kid_on_the_block)

    def indent(self):
        """ indent a group of selected text or the current block """
        self.dent(de=False)


    def deIndent(self):
        """ de-indent the selected text or current block """
        self.dent(de=True)


    def blockMove(self, direction):
        """ move the current block up or down """

        cursor = self.textEdit.textCursor()
        block = cursor.block()

        if direction == + 1:
            swap_with = block.previous()

        elif direction == - 1:
            swap_with  = block.next()

        inblock_pos   = cursor.positionInBlock()
        swap_with_pos = swap_with.position()
        block_pos     = block.position()

        block      = block.blockNumber()
        swap_with  = swap_with.blockNumber()

        text   = self.textEdit.toPlainText()
        blocks = text.split('\n')

        block_text = blocks[block]
        swap_with_text = blocks[swap_with]

        blocks[block] = swap_with_text
        blocks[swap_with] = block_text

        self.textEdit.setPlainText(''.join([blk+'\n' for blk in blocks]))

        if direction == -1:
            cursor.setPosition(block_pos + inblock_pos + len(swap_with_text+'\n'))

        elif direction == +1:
            cursor.setPosition(swap_with_pos + inblock_pos)

        self.textEdit.setTextCursor(cursor)

    def braceHelper(self, keycode):
        """ when you click a brace key, make the enclosing one automatically"""

        if keycode == QtCore.Qt.Key_ParenLeft:   # ()
            text = "()"
        elif keycode == QtCore.Qt.Key_BracketLeft: # []
            text = "[]"
        elif keycode == QtCore.Qt.Key_BraceLeft:  # {}
            text = "{}"

        csr = self.textEdit.textCursor()
        csr.insertText(text)
        csr.movePosition(QtGui.QTextCursor.PreviousCharacter)
        self.textEdit.setTextCursor(csr)

    def textCursorChange(self):
        """ actions upon change of cursor position """

        self.highlighter.braceMatcher()
        """ Once upon a time, there was a guy named Jonny.
            He spent way too many hours trying to get brace match highlighting
            working in PyQt. He tried at least 10 separate full implementations
            all of which failed in some key metric.

            Hours of work, hours of planning - scheming - designing later, he
            pieced together a robust, fast architecture.

            Excited, he finally wrote the algorithm, to find braces matches!

            But alas, the hilariously, ridiculously, comically, preposterously
            limited nature of text formatting in PyQt's QTextEdit and
            QSyntaxHighlighter classes forced Jonny to put that feature on hold.

            He discovered, curiously, that PyQt's formatting functionality
            often simply does not work - particularly, formatting a color only
            works if one is actually typing (cannot be done programmatically),
            and disemboldening a character fails if its neighboring character
            is emboldened.

            His 2 full-work-days-long dream of highlighting matching brackets
            was shattered upon arrival - and he moved on to do greater things.

            RIP self.highlighter.braceMatcher, Nov 20 2017 - Nov 21 2017
            -------------------------------------------------------------------
            ---------------------------- EPILOGUE -----------------------------
            -------------------------------------------------------------------
                   On Nov 22 2017, at 1813 UTC, a breakthrough was made!

            Jonny realized that the reason disemboldening characters was broken,
            was that : in the changing of the textEdit body all recorded END
            brace indices were falsified! By intercepting the text update
            BEFORE it occurs (in the ActionWatcher), he could clear all
            highlights with their properly recorded indices. Then Qt could
            proceed to update the textedit's body.

            So, if you're going through hell, keep going!

            "Restlessness and discontent are the first necessities of progress.
            Show me a thoroughly satisfied man, and I will show you a failure"
                - Thomas Edison

            "The most certain way to succeed
                is always to try just one more time" - Thomas Edison
        """

    def saveState(self,state):
        """ keep track of save state in title """

        if state:
            if self.windowTitle()[-1] == '*':
                self.setWindowTitle(self.windowTitle()[:-1])
        else:
            if self.windowTitle()[-1] != '*':
                self.setWindowTitle(self.windowTitle()+'*')

    def isSaved(self):
        """ is the current file saved? """

        if self.windowTitle()[-1] == '*':
            return False
        else:
            return True

    def setupFont(self):
        """ Set the font for the editor """

        self.editor_font = QtGui.QFont()
        self.editor_font.setFamily('Fira Mono')
        self.editor_font.setStyleHint(QtGui.QFont.Monospace)
        self.editor_font.setFixedPitch(True)
        self.textEdit.setFont(self.editor_font)

        metrics = QtGui.QFontMetrics(self.editor_font)
        self.textEdit.setTabStopWidth(4 * metrics.width(' '))

        self.setFontSize()

    @pyqtSlot()
    def changeFontSize(self, direction):
        """ Change font size, duh! :) """

        if direction > 0:
            self.fontsize +=1
        elif direction < 0:
            self.fontsize -=1

        if self.fontsize < 1:
            self.fontsize = 1

        self.setFontSize()

    def setFontSize(self):
        """ Behold, the world's janky-est way to set font size """

        start_cursor_pos = self.textEdit.textCursor().position()

        # self.textEdit.selectAll()

        self.editor_font.setPointSize(self.fontsize) # keep active editor font
        self.textEdit.setFontPointSize(self.fontsize)

        d = self.textEdit.document()
        d.setDefaultFont(self.editor_font)
        self.textEdit.setDocument(d)

        self.textEdit.setPlainText(self.textEdit.toPlainText())

        # get tab size right
        metrics = QtGui.QFontMetrics(self.editor_font)
        self.textEdit.setTabStopWidth(4 * metrics.width(' '))

        # reset cursor position to start
        c = self.textEdit.textCursor()
        c.setPosition(start_cursor_pos)
        self.textEdit.setTextCursor(c)

        # inform higlighter
        self.highlighter.setFontSize(self.fontsize)

        # set default to current
        self.changeDefault('font_size', self.fontsize)

        #print('set font size to:', self.fontsize)
        #print('act font size is:', self.textEdit.fontPointSize())

    def launch(self):
        """ launch the program """
        if self.file == '' or self.windowTitle()[-1]=='*':
            self.save()

        if self.file != '': # can still happen if user canceled save

            if self.system == 'Windows':
                os.system('start cmd /K python "'+self.file+'"')
            else:
                Popen('python "'+self.file+'"', shell=True)

    def new(self):
        """ new program """
        self.openNew()

    def open(self, no_dialog=False):
        """ open a program """

        if not no_dialog:

            self.o_file = QtWidgets.QFileDialog.getOpenFileName(self,
                                                                'Open Python File',
                                                                filter = '*.py',
                                                                directory = self.file)

            self.o_file = self.o_file[0]  # 0 = path, 1 = format

        # if no file yet opened, or opening procedurally, open here
        if self.file == '' or (self.file !='' and no_dialog):

            if self.file == '' and not no_dialog:
                self.file = str(self.o_file)

            try:
                with open(self.file,'r',encoding="utf-8") as f:

                    try:
                        open_file_text = f.read()

                    except Exception as e:
                        self.newMessage("Make Python couldn't open because "+
                                        str(e))
                        self.file = ''
                        return

                    # now replace quad spaces with \t for save consistency
                    open_file_text = open_file_text.replace('    ','\t')

                    self.textEdit.setPlainText(open_file_text)

                    self.textChange()

            except FileNotFoundError:
                return

            try:
                title = ''.join([self.file[self.file.rindex("\\")+1:],' — Make Python Editor'])
                self.setWindowTitle(title)
            except ValueError:
                title = ''.join([self.file[self.file.rindex("/")+1:],' — Make Python Editor'])
                self.setWindowTitle(title)

        else: # if file already opened, open in new window
            self.openNew()

    def openNew(self):
        """ open new window """

        if hasattr(self,'o_file') and self.o_file != self.file:
            Popen(['makepython', self.o_file])
        else:
            Popen(['makepython'])

    def save(self, save_as=False):
        """ save the program """

        if self.file == '' or save_as:
            self.file = QtWidgets.QFileDialog.getSaveFileName(self,
                                           'Save Python File', filter = '*.py')

            self.file = self.file[0]  # 0 = path, 1 = format

        if self.file != '':

            editor_text = self.textEdit.toPlainText()

            # Convert all '\t' characters into quad spaces
            editor_text = editor_text.replace('\t','    ')

            f = open(self.file, 'w', encoding='utf-8')
            f.write(editor_text)
            f.close()

            try:
                title = ''.join([self.file[self.file.rindex("\\")+1:],
                                ' — Make Python Editor'])
                self.setWindowTitle(title)
            except ValueError:
                title = ''.join([self.file[self.file.rindex("/")+1:],
                                ' — Make Python Editor'])
                self.setWindowTitle(title)

            self.saveState(1)

    def toSaveOrNotToSave(self, event):
        """ open option dialog with save, leave, and cancel options """
        self.option = opt.Option(
                                    {   'left'   : 'Save',
                                        'right'  : 'Leave'  },

                                      { 'cancel' : event.ignore,
                                        'left'   : self.save,
                                        'right'  : lambda: None, }, self)

    def closeEvent(self,event):
        """ upon window close """
        if not self.isSaved():
            self.toSaveOrNotToSave(event)

        # delete the temporary file which we use to run commands in shell
        # with selections
        if os.path.isfile('run_in_shell.py'):
            os.remove('run_in_shell.py')

    def newShell(self):
        """ launch a python shell. if text highlighted, run it first"""

        if self.textEdit.textCursor().hasSelection():

            to_run = self.textEdit.textCursor().selectedText()
            to_run = to_run.replace(u"\u2029",'\n')  # QString --> utf-8

            with open('run_in_shell.py','w',encoding='utf-8') as temp_py:
                temp_py.write(to_run)

            command = 'python -i run_in_shell.py'

        else:
            command = 'python'

        if self.system == 'Windows':
            os.system('start cmd /K ' + command)

        else:
            Popen(command, shell=True)

    def findSource(self):
        """ find the source of the highlighted function """

        cursor = self.textEdit.textCursor()
        selected = cursor.selection()

        if selected.isEmpty():
            cursor.select(QtGui.QTextCursor.WordUnderCursor)
            selected = cursor.selectedText()
            self.textEdit.setTextCursor(cursor)
        else:
            selected = selected.toPlainText()

        try:
            spec = importlib.util.spec_from_file_location(
                                            self.file[self.file.rindex('/')+1:-3],
                                            self.file)
        except ValueError:
            try:
                spec = importlib.util.spec_from_file_location(
                                                self.file[self.file.rindex('\\')+1:-3],
                                                self.file)
            except Exception as e:
                self.newMessage("Make Python couldn't find this file. Have you saved yet?")
                return

        module = importlib.util.module_from_spec(spec)

        # don't allow execution of file unless there is a __name__ == main argument
        # without doing this, the program would be run within the Make Python thread!
        # (this is because python imports files by executing them)

        # we check here to make sure there is some certainty of
        # import execution protection... execute import & open source if:

        #  -> if there's an if __name__=='__main__' argument
        #  -> if we're inside some module's __init__ file
        #     -> we assume module devs made good decisions w.r.t. import exec

        with open(self.file,'r',encoding='utf-8') as f:
            content = f.read()

        content = content.replace(' ','').replace('"','').replace("'",'')

        if ("""if__name__==__main__""" in content
                              or
                    spec.name == '__init__'):

            try:
                spec.loader.exec_module(module)
            except Exception as e:
                self.newMessage("Couldn't find source because"+str(e))
        else:
            self.newMessage('''Sorry, can't do search without any'''+
                            ''' import execution protection like >''' +
                            ''' if __name__=="__main__"''')
            return

        try:
            self.o_file = inspect.getfile(getattr(module,selected))

            if self.o_file != self.file:
                if self.o_file[-2:] == 'py':  # can't open precompiled stuff
                    self.openNew()
                else:
                    self.newMessage("Make Python can't edit the "+
                                    self.o_file[self.o_file.index('.'):]+
                                    " file at " + self.o_file)
            else:
                self.find()

                if inspect.isfunction(getattr(module,selected)):
                    self.findText.setPlainText('def '+selected)

                elif inspect.isclas(getattr(module,selected)):
                    self.findText.setPlainText('class '+selected)

                self.findTextChange()

        except Exception as e:
            self.newMessage("Make Python can't edit source because "+str(e))


    def openPIP(self):
        """ open the window which allows pip installs """
        self.pip = pip.PipBar()

    def find(self):
        """ open find/replace text widget """

        opened_height = 25
        self.findandreplace_findbutton.setFixedHeight(opened_height)
        self.findandreplace_closebutton.setFixedHeight(opened_height)
        self.findandreplace_replacebutton.setFixedHeight(opened_height)
        self.replaceText.setFixedHeight(opened_height)
        self.findText.setFixedHeight(opened_height)
        self.findText.setFocus()

    def closeFindShortcut(self):
        """ allow escape to close if find/replace active """
        if self.findText.height() != 0:
            self.closeFind()

    def closeFind(self):
        """ close find/replace text widget """
        closed_height = 0
        self.findandreplace_findbutton.setFixedHeight(closed_height)
        self.findandreplace_closebutton.setFixedHeight(closed_height)
        self.findandreplace_replacebutton.setFixedHeight(closed_height)
        self.replaceText.setFixedHeight(closed_height)
        self.findText.setFixedHeight(closed_height)

    def findTextChange(self,force=False):
        """ text find box changed """
        text = self.findText.toPlainText()
        if '\n' in text or force:

            # prevent newlines
            if not force:
                text = text.replace('\n','')

            c = self.findText.textCursor()
            self.findText.setPlainText(text)
            self.findText.setTextCursor(c)

            reset_cursor = self.textEdit.textCursor()
            if not reset_cursor.hasSelection():
                reset_cursor.setPosition(0)

            self.textEdit.setTextCursor(reset_cursor)
            found = self.textEdit.find(text)  # then search forwards

            if not found:
                reset_cursor = self.textEdit.textCursor()
                reset_cursor.setPosition(0)
                self.textEdit.setTextCursor(reset_cursor)

    def replaceTextChange(self,force=False):
        """ text replace box changed """

        text = self.replaceText.toPlainText()

        if '\n' in text or force:

            # prevent new lines
            if not force:
                text = text.replace('\n','')

            c = self.replaceText.textCursor()
            self.replaceText.setPlainText(text)
            self.replaceText.setTextCursor(c)

            if (self.textEdit.textCursor().selection().toPlainText()
                            !=
                self.findText.toPlainText()):

                self.findTextChange(force=True)

            else:
                # replace text
                selected = self.textEdit.textCursor()
                selected.insertText(text)

    def newMessage(self,text):
        """ send a message to the person using the program.

            messages should be so simple that they can be understood
            within 5 seconds. messages can only be 1 line long.

            don't panic!
        """
        self.messageText.setPlainText(str(text))
        self.messageText.setVisible(1)

        self.message_timer = QtCore.QTimer()
        self.message_timer.timeout.connect(self.closeMessage)
        self.message_timer.start(defaults.message_time*1000)

    def closeMessage(self):
        """ close the message box after timeout """
        self.messageText.setVisible(0)
        self.message_timer.stop()

    def flipTheme(self,override=False):
        """ switch from light to dark theme """

        if not override:
            self.color_mode = not self.color_mode

        utils.changeCSS(self,'background',
        styles.ui_colors[self.color_mode]['bg_window'])

        utils.changeCSS(self.textEdit,'color',
        styles.syntax_colors[self.color_mode]['default'])

        utils.changeCSS(self.textEdit,'background',
        styles.ui_colors[self.color_mode]['bg_textEdit'])

        utils.changeCSS(self.messageText,'color',
        styles.syntax_colors[self.color_mode]['default'])

        utils.changeCSS(self.messageText,'background',
        styles.ui_colors[self.color_mode]['bg_textEdit'])

        utils.changeCSS(self.pybutton,'color',
        styles.ui_colors[self.color_mode]['py_color'])

        for button in self.buttons:

            utils.changeCSS(button,'background-color',
            styles.ui_colors[self.color_mode]['bg_button'])

            utils.changeCSS(button,'border',
            styles.ui_colors[self.color_mode]['bd_button'])

        self.highlighter = syntax.PythonHighlighter(self.textEdit, self.color_mode)

        self.changeDefault('color_mode',self.color_mode)

    def changeDefault(self,var_name,value):
        """ change a value in the defaults file """

        # python "with" statement for files appears to be broken...?
        # can't seem to find the __enter__ method. Weird

        try:
            f = open(self.root + 'defaults.py','r',encoding='utf-8')
            txt = f.read()
            beg = txt.index(var_name)
            end = txt.index('\n',txt.index(var_name))
            col = txt[beg:end]
            txt = txt.replace(col, var_name + ' = ' + str(value))
            f.close()

            f = open(self.root + 'defaults.py','w',encoding='utf-8')
            f.write(txt)
            f.close()

        except OSError as e:
            self.newMessage('error setting new default because'+str(e))


if __name__=='__main__':

    app = QtWidgets.QApplication(sys.argv)
    gui = Interface(sys.argv)
    gui.show()
    app.exec_()
