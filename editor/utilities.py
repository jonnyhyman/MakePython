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
