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

from subprocess import Popen
import platform
import winreg
import os

# logging

def add_to_log(farg, *args):

    x = ''.join([str(farg)+' '] + [ str(arg)+' ' for arg in args ])

    with open('INSTALL.log','a') as f:
        f.write(' ' + str(x) + '\n')

print = add_to_log

#--------------------------------------------------- qt qss / css changing

def extractCSS(style,att):
    beg   = style.index(att)+len(att)+1 # don't include :
    end   = style.index(';',beg) # don't include ';'
    return style[beg:end]

def changeCSS(obj,attribute,target):
    style = obj.styleSheet()
    style = style.replace(extractCSS(style,attribute),target)
    obj.setStyleSheet(style)

#  -------------------------------------------------- check the size of a dir

def folderSizePercentage(folder_path, END_SIZE):

    if os.path.exists(folder_path):
        ACT_SIZE = 0

        for dirpath, dirnames, filenames in os.walk(folder_path):
            #print(dirpath,dirnames)
            if dirnames != '__pycache__':
                for f in filenames:
                    try:
                        fp = os.path.join(dirpath, f)
                        ACT_SIZE += os.path.getsize(fp)
                    except:
                        continue

        PCT_DONE = ACT_SIZE / END_SIZE # actual/target
        PCT_DONE *= 100

        if PCT_DONE > 100:
            PCT_DONE = 100

        return PCT_DONE
    else:
        return 0

# ---------------------------------------------------- function to set PATH

def set_env_path(new_path=None, append_to_path=None, prepend_to_path=None,
                 delete_from_path=None):
    """ Here we set the SYSTEM path variable (persitently) """

    if platform.system() == 'Windows':

        # We don't want to accidentally set all USER path variables into
        # system path (os.environ['Path'] concatenates the USER and SYSTEM
        # Path variables on windows). So we actually look in the registry
        # for the current SYSTEM Env Path

        reg_path = r'Environment'
        usr_path = get_usr_reg('PATH',reg_path)
        if usr_path is not None:
            print('current environment path looks like:')
            [print('   '+var) for var in usr_path.split(';')]
        else:
            print('could not gather environment path from registry... :(')

    else:
        usr_path = os.environ['PATH']

    setvar = False

    if new_path is not None:  ## AVOID USING THIS EXECUTION PATH!
        if new_path != usr_path:
            setvar = True

    elif append_to_path is not None:
        if append_to_path not in usr_path:

            new_path = usr_path

            if usr_path[-1]!=';':
                new_path += ';' + append_to_path
            else:
                new_path += append_to_path

            setvar = True

    elif prepend_to_path is not None:
        if prepend_to_path not in usr_path:

            new_path = prepend_to_path

            if new_path[-1] != ';':
                new_path += ';' + usr_path
            else:
                new_path += usr_path

            setvar = True

    elif delete_from_path is not None:
        if delete_from_path in usr_path:

            if ';'+delete_from_path in usr_path:
                prefix = ';'
            else:
                prefix=''

            if delete_from_path+';' in usr_path:
                suffix = ';'
            else:
                suffix = ''


            new_path = usr_path.replace(prefix + delete_from_path + suffix, '')
            setvar = True

    if setvar:

        if platform.system() == 'Windows':

            print('setting sys environment path to:')
            [print('   '+var) for var in new_path.split(';')]

            if set_usr_reg('PATH', new_path, reg_path):
                print('setting sys environment path succeeded!')
            else:
                print('setting sys environment path failed!')

        else:

            print('UNIX support forthcoming!')

    else:
        print('attempted set_env_path but setvar was False')


def set_usr_reg(name, value, REG_PATH):  # REGPATH MUST BE RAW STRING
    """ Set the input local registry key """

    try:

        print('SET_REG >> SET [', REG_PATH, '] KEY "', name,'" TO', value)

        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH,
                                        0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)

        return True

    except WindowsError as e:
        print(e)
        return None

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

def set_context_menu(mp_exec, undo=False):
    """ Create Windows context menu item alongside IDLE """


    if not undo:
        try:


            REG_PATH = 'Python.File\\Shell\\Edit with Make Python\command'
            COMMAND  = '''"''' + mp_exec + '''" %L'''
            NAME = '' # (Default)

            print('SET_REG >> SET [', REG_PATH, '] KEY "', NAME,'" TO', COMMAND)

            # looks like: pydir\Lib\site-packages\makepython\makepython.exe %L

            winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, REG_PATH)
            registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH,
                                            0, winreg.KEY_WRITE)

            winreg.SetValueEx(registry_key, NAME, 0, winreg.REG_SZ, COMMAND)

            winreg.CloseKey(registry_key)

            return True

        except WindowsError as e:
            print(e)
            return None
    else:

        try:

            # This stuff is not in a function because I have no intention
            # of reusing it anywhere else!

            # ---------------- first delete subkey

            REG_PATH = 'Python.File\\Shell\\Edit with Make Python\\command'
            NAME = '' # (Default)

            print('SET_REG >> DEL [', REG_PATH, '] KEY')


            # looks like: pydir\Lib\site-packages\makepython\makepython.exe %L

            registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH,
                                            0, winreg.KEY_ALL_ACCESS)

            winreg.DeleteKey(registry_key, NAME)
            winreg.CloseKey(registry_key)

            # --------------- then delete main key

            REG_PATH = 'Python.File\\Shell\\Edit with Make Python'
            NAME = '' # (Default)

            print('SET_REG >> DEL [', REG_PATH, '] KEY')


            # looks like: pydir\Lib\site-packages\makepython\makepython.exe %L

            registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH,
                                            0, winreg.KEY_ALL_ACCESS)

            winreg.DeleteKey(registry_key, NAME)
            winreg.CloseKey(registry_key)

            return True

        except WindowsError as e:
            print(e)
            return None

def get_makepython_dir():
    """ We use this to find where the current file, makepython.exe
        exists (from folders in system environment path) """

    print('looking for makepython.executable in path directories...')

    if platform.system() == 'Windows':
        path = get_usr_reg('PATH',r'Environment')

    else:
        path = os.environ['Path']

    for folder in path.split(';'):

        if platform.system() == 'Windows':
            executable = '\\makepython.exe'
        else:
            executable = '\\makepython'

        print('trying :', folder + executable)

        if os.path.isfile(folder + executable):
            print('found makepython.executable!')
            return folder
