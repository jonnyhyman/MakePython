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
