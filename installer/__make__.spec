# -*- mode: python -*-

block_cipher = None

add_to_datas = [

    ('C:\\Python36-64\\lib\\site-packages\\PyQt5\\Qt\\bin\\Qt5Core.dll','.'),
    ('C:\\Python36-64\\lib\\site-packages\\PyQt5\\Qt\\bin\\Qt5Gui.dll','.'),
    ('C:\\Python36-64\\lib\\site-packages\\PyQt5\\Qt\\bin\\Qt5Widgets.dll','.'),
    ('C:\\Python36-64\\lib\\site-packages\\PyQt5\\Qt\\bin\\libEGL.dll','.'),
    ('fonts','fonts')

]

a = Analysis(['__make__.py'],
             pathex=['C:\\Users\\__jonny__\\Dropbox\\Compute\\makepython\\code',
                     'C:\\Python36-64\\Lib\\site-packages\\PyQt5\\Qt\\bin'],
             binaries=[],
             datas=add_to_datas,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)


exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Make Python Installer',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='icon.ico')
