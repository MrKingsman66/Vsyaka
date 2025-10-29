# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['temp_build\\bot_modified.py'],
    pathex=[],
    binaries=[],
    datas=[('temp_build\\service_account.json', '.')],
    hiddenimports=['google.oauth2.service_account', 'gspread', 'aiogram', 'aiogram.filters', 'aiogram.types', 'asyncio'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='KingsmanRentBot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
