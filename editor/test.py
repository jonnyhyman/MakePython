import platform
import os

for folder in os.environ['Path'].split(';'):

    if platform.system() == 'Windows':
        executable = '\\python.exe'
    else:
        executable = '\\python'

    print('trying :', folder + executable)

    if os.path.isfile(folder + executable):
        print('found python!')

        mk_pkg = '\\Lib\\site-packages\\makepython'

        if os.path.isdir(folder + mk_pkg):
            print('found makepython folder!',folder+mk_pkg)

            if platform.system() == 'Windows':
                executable = '\\makepython.exe'
            else:
                executable = '\\makepython'

            if os.path.isfile(folder + mk_pkg + executable):
                print('found makepython.exe!',folder + mk_pkg + executable)
                return folder + mk_pkg

            else:
                print('''couldn't find makepyhton.exe :(''')
