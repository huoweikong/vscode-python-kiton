# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['F:\\vscode-python-kiton\\实验室数据分析\\病毒学相关\\my_TCID50-4.0.py'],
             pathex=['F:\\vscode-python-kiton'],
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
          [],
          exclude_binaries=True,
          name='my_TCID50-4.0',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='my_TCID50-4.0')
