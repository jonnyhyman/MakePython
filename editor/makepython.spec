# -*- mode: python -*-

# UPDATE PROCESS:
# 1. Update makepython.py
# 2. Update makepython.spec as needed
# 3. Run pyinstaller makepython.spec
# 4. Copy makepython.exe from dist into main directory
# 5. Compress main directory files into a zip
# 6. Place Dropbox link to zip in __make__.install_globals
# 7. Run pyinstaller __make__.spec
# 8. Distribute __make__.exe as "Install Make Python"

block_cipher = None

add_to_datas = [

    ('C:\\Python36-64\\lib\\site-packages\\PyQt5\\Qt\\bin\\Qt5Core.dll','.'),
    ('C:\\Python36-64\\lib\\site-packages\\PyQt5\\Qt\\bin\\Qt5Gui.dll','.'),
    ('C:\\Python36-64\\lib\\site-packages\\PyQt5\\Qt\\bin\\Qt5Widgets.dll','.'),
    ('C:\\Python36-64\\lib\\site-packages\\PyQt5\\Qt\\bin\\libEGL.dll','.'),
    ('fonts','fonts')

]

a = Analysis(['makepython_windows.py'],
             pathex=[
             'C:\\Users\\__jonny__\\Dropbox\\Compute\\makepython\\code\\editor',
             'C:\\Python36-64\\Lib\\site-packages\\PyQt5\\Qt\\bin'
             ],
             binaries=[],
             datas=add_to_datas,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher = block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='makepython',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='icon.ico')
