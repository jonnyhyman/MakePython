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

"""
    Making a change? Here's the make-change checklist!
        1. Make change as needed
            1.1 make sure the folder zipped has same name as zip_nam

        2. pyinstaller __make__.spec
        3. test locally
        4. test remotely / fresh install
"""

zip_nam = 'editor-2-0-0'
zip_url = ("https://github.com/jonnyhyman/MakePython/files/1840351/"
            "editor-2-0-0.zip")

pythonorg_root = "https://www.python.org/ftp/python/"
pip_dependencies = {'PyQt5':'pyqt5'} # foldername / pypi name
delete_log_after = False

# Latest stable Python Version Number is input below

# The version must support both PyQt5 and sip to work
# and the PyQt5 / sip versions on PyPI

V = '3'
R = '6.4'
