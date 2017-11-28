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

from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter
from PyQt5.QtGui import QTextCursor, QBrush
import utilities as utils
import defaults
import styles

def char_format(color, style=''):
    """Return a QTextCharFormat with the given attributes.
    """
    c_color = QColor()
    c_color.setNamedColor(color)

    c_format = QTextCharFormat()
    c_format.setForeground(c_color)

    if 'bold' in style:
        c_format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        c_format.setFontItalic(True)

    return c_format

class PythonHighlighter (QSyntaxHighlighter):
    """ Syntax highlighter for the Python language.
        Courtesy of http://bit.ly/2j6ouqV """

    # Python keywords
    keywords = [
        'and', 'assert', 'break', 'class', 'continue', 'def',
        'del', 'elif', 'else', 'except', 'exec', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in',
        'is', 'lambda', 'not', 'or', 'pass', 'print',
        'raise', 'return', 'try', 'while', 'yield',
        'None', 'True', 'False', 'with', 'as', 'TODO:',

    ]

    builtins = [
        '__init__','dict','str','bytes','tuple','list','float','int','long'
    ]

    # Python operators
    operators = [
        '=',
        # Comparison
        '==', '!=', '<', '<=', '>', '>=',
        # Arithmetic
        '\+', '-', '\*', '/', '//', '\%', '\*\*',
        # In-place
        '\+=', '-=', '\*=', '/=', '\%=',
        # Bitwise
        '\^', '\|', '\&', '\~', '>>', '<<',
    ]

    # Python braces
    braces = [
        '\{', '\}', '\(', '\)', '\[', '\]',
    ]

    highlighted_braces = []

    def __init__(self, document, color_mode):

        QSyntaxHighlighter.__init__(self, document)

        self.document = document

        # Multi-line strings (expression, flag, style)
        # FIXME: The triple-quotes in these two lines will mess up the
        # syntax highlighting from this point onward

        self.color_mode = color_mode
        self.fontsize = defaults.font_size

        self.STYLES = {
            'keyword' : char_format(*styles.syntax_colors[color_mode]['keyword']),
            'builtins': char_format(*styles.syntax_colors[color_mode]['builtins']),
            'operator': char_format(*styles.syntax_colors[color_mode]['operator']),
            'brace'   : char_format(*styles.syntax_colors[color_mode]['brace']),
            'brace_h' : char_format(*styles.syntax_colors[color_mode]['brace_h']),
            'defclass': char_format(*styles.syntax_colors[color_mode]['defclass']),
            'string'  : char_format(*styles.syntax_colors[color_mode]['string']),
            'string2' : char_format(*styles.syntax_colors[color_mode]['string2']),
            'comment' : char_format(*styles.syntax_colors[color_mode]['comment']),
            'self'    : char_format(*styles.syntax_colors[color_mode]['self']),
            'numbers' : char_format(*styles.syntax_colors[color_mode]['numbers']),
        }

        self.tri_single = (QRegExp("'''"), 1, self.STYLES['string2'])
        self.tri_double = (QRegExp('"""'), 2, self.STYLES['string2'])

        rules = []

        # Keyword, builtins operator, and brace rules
        rules += [(r'\b%s\b' % w, 0, self.STYLES['keyword'])
            for w in PythonHighlighter.keywords]
        rules += [(r'\b%s\b' % w, 0, self.STYLES['builtins'])
            for w in PythonHighlighter.builtins]
        rules += [(r'%s' % o, 0, self.STYLES['operator'])
            for o in PythonHighlighter.operators]
        rules += [(r'%s' % b, 0, self.STYLES['brace'])
            for b in PythonHighlighter.braces]

        # All other rules
        rules += [
            # 'self'
            (r'\bself\b', 0, self.STYLES['self']),

            # Double-quoted string, possibly containing escape sequences
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, self.STYLES['string']),
            # Single-quoted string, possibly containing escape sequences
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, self.STYLES['string']),

            # 'def' followed by an identifier
            (r'\bdef\b\s*(\w+)', 1, self.STYLES['defclass']),
            # 'class' followed by an identifier
            (r'\bclass\b\s*(\w+)', 1, self.STYLES['defclass']),

            # From '#' until a newline
            (r'#[^\n]*', 0, self.STYLES['comment']),

            # Numeric literals
            (r'\b[+-]?[0-9]+[lL]?\b', 0, self.STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, self.STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0,
                                                        self.STYLES['numbers']),
        ]

        # Build a QRegExp for each pattern
        self.rules = [(QRegExp(pat), index, fmt)
            for (pat, index, fmt) in rules]

    def setFontSize(self, size):
        self.fontsize = size
        self.clearBraceHighlights()  # otherwise they'll retain their style

    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text."""

        # Do other syntax formatting
        for expression, nth, char_format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, char_format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # Do multi-line strings
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

    def match_multiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line things. ``delimiter`` should be a
        ``QRegExp`` for triple-single-quotes or triple-double-quotes, and
        ``in_state`` should be a unique integer to represent the corresponding
        state changes when inside those things. Returns True if we're still
        inside a multi-line string when this function is finished.
        """
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
            # Move past this match
            add = delimiter.matchedLength()

        # As long as there's a delimiter match on this line...
        while start >= 0:
            # Look for the ending delimiter
            end = delimiter.indexIn(text, start + add)
            # Ending delimiter on this line?
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            # No; multi-line string
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            # Apply formatting
            self.setFormat(start, length, style)
            # Look for the next match
            start = delimiter.indexIn(text, start + length)

        # Return True if still inside a multi-line string, False otherwise
        if self.currentBlockState() == in_state:
            return True
        else:
            return False

    def braceSearch(self, text, block, in_block_pos, search_direction):
        ''' search for start and end braces '''
        count = 1
        search_block = block
        total_number_of_blocks = len(self.document.toPlainText().split('\n'))

        if search_direction == 1:
            max_steps = total_number_of_blocks - block.blockNumber()
        else:
            max_steps = block.blockNumber() + 1

        for b in range(max_steps):

            search_block_text = search_block.text()

            #print('  checking block #',search_block.blockNumber(),'-->',list(search_block_text))

            if (utils.brotherBrace(text[in_block_pos-1]) in search_block_text
                                 or text[in_block_pos-1] in search_block_text):

                if search_block == block:
                    if search_direction == +1:
                        search_start_index = in_block_pos
                    if search_direction == -1:
                        search_start_index = len(search_block_text)-(in_block_pos-1)
                else:
                    search_start_index = 0

                #print('   start index is',search_start_index)

                if len(search_block_text) > 0:

                    if search_direction == -1:
                        # text_length is required b/c reversed() has no length
                        text_length        = len(search_block_text)
                        search_block_text  = reversed(search_block_text)

                    for n, c in enumerate(search_block_text):

                        if n < search_start_index and search_direction == +1:
                            #print('        skipping',n,c)
                            continue
                        elif n < search_start_index and search_direction == -1:
                            #print('        skipping',n,c)
                            continue

                        #print('        ',n,c)

                        if c == utils.brotherBrace(text[in_block_pos-1]):
                        #    print('           ',c,'==',
                        #utils.brotherBrace(text[in_block_pos-1]),'->',count)
                            count -= 1
                        #else:
                        #    print('           ',c,'!=',
                        #utils.brotherBrace(text[in_block_pos-1]),'->',count)

                        if c == text[in_block_pos-1]:
                            count += 1

                        if count == 0:
                            if search_direction == -1:
                                n = text_length - (n+1)
                            return search_block, n # n is the in-block position

            if search_direction == +1:
                search_block = search_block.next()
            else:
                search_block = search_block.previous()

        return None, None

    def braceMatcher(self):
        ''' Do brace matching for all kinds of braces '''

        cursor = self.document.textCursor()
        in_block_pos = cursor.positionInBlock()
        block  = cursor.block()
        text   = block.text()

        if len(text)>0 and (text[in_block_pos-1] in ['{','[','(','}',']',')']):

            #print('  start : inblock-->',in_block_pos-1,'| blockN-->',
            #block.blockNumber(),'| got brace -->',text[in_block_pos-1])

            if text[in_block_pos-1] in ['{','[','(']: # look forwards

                end_block, end_in_block_pos = self.braceSearch(text,
                                                               block,
                                                               in_block_pos,
                                                               1)

            else:
                if in_block_pos > 0:
                    end_block, end_in_block_pos = self.braceSearch(text,
                                                                   block,
                                                                   in_block_pos,
                                                                   -1)
                else:
                    end_block = None

            #if end_block is not None:
                #print('  end   : inblock-->',end_in_block_pos,'| blockN-->',
                #end_block.blockNumber(),'| in text -->',end_block.text())
            #else:
                #print('  no end')

            # now that we know where the start / end are, style them!

            csr = self.document.textCursor()
            csr.joinPreviousEditBlock()  # this is critical to maintaining
                                         # a correct undo/redo log

            if end_block is not None:
                self.setBraceFormats(csr,[(block, in_block_pos-1, True),
                                          (end_block, end_in_block_pos, True)])

            else:

                self.setBraceFormats(csr,
                                     [(block, in_block_pos-1, False)])

            csr.endEditBlock()  # end with respect to joinPreviousEditBlock

        else:

            self.clearBraceHighlights()

    def clearBraceHighlights(self):
        ''' Clear all highlighted braces '''

        braces = []
        for n, block_in_block_pos in enumerate(self.highlighted_braces):

            block, in_block_pos = block_in_block_pos
            braces.append((block, in_block_pos, False))

        csr = self.document.textCursor()
        csr.joinPreviousEditBlock()  # this is critical to maintaining
                                     # a correct undo/redo log

        self.setBraceFormats(csr, braces)
        self.highlighted_braces = [] # reset

        csr.endEditBlock()  # end with respect to joinPreviousEditBlock

    def setBraceFormats(self, csr, braces):
        ''' Set a bunch of brace formats '''

        for brace in braces:

            block, in_block_pos, highlight = brace

            # navigate to the brace and select it

            #csr = self.document.textCursor()
            csr.setPosition(block.position() + in_block_pos) # absolute
            csr.movePosition(QTextCursor.NextCharacter,  # select brace
                      mode = QTextCursor.KeepAnchor)

            #print('  highlighting :' if highlight else '  unhighlighting :',
            #     csr.selection().toPlainText(), 'at', in_block_pos)

            if highlight:

                self.STYLES['brace_h'].setFontPointSize(self.fontsize)

                csr.setCharFormat(self.STYLES['brace_h'])
                self.highlighted_braces.append((block, in_block_pos))

            else:

                self.STYLES['brace'].setFontPointSize(self.fontsize)

                csr.setCharFormat(self.STYLES['brace'])
