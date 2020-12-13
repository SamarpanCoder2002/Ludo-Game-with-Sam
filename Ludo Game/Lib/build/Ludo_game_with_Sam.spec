# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Ludo_game_with_Sam.py'],
             pathex=["C:\\Users\\Don't tuch\\.PyCharmCE2018.3\\config\\scratches\\Tkinter_files\\Ludo Game"],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Ludo_game_with_Sam',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='Images\\ludo_icon.ico')
