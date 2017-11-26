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

import winreg

def extractCSS(style,att):
    beg   = style.index(att)+len(att)+1 # don't include :
    end   = style.index(';',beg) # don't include ';'
    return style[beg:end]

def changeCSS(obj,attribute,target):
    style = obj.styleSheet()
    style = style.replace(extractCSS(style,attribute),target)
    obj.setStyleSheet(style)

def brotherBrace(brace):
    if brace == '[':
        return ']'
    elif brace == ']':
        return '['
    elif brace == '(':
        return ')'
    elif brace == ')':
        return '('
    elif brace == '{':
        return '}'
    elif brace == '}':
        return '{'

def get_usr_reg(name, REG_PATH):  # REGPATH MUST BE RAW STRING
    """ Get the value of the local registry key """

    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH,
                                        0, winreg.KEY_READ)

        value, regtype = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        return value

    except WindowsError as e:
        print(e)
        return None
