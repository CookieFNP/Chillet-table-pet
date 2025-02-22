# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['init_multiple_U.py'],
    pathex=[],
    binaries=[],
    datas=[('KUM', 'KUM'), ('yunKUM', 'yunKUM'), ('angryKUM', 'angryKUM'), ('cryKUM', 'cryKUM'), ('danceKUM', 'danceKUM'), ('jumpKUM', 'jumpKUM'), ('lookKUM', 'lookKUM'), ('tieKUM', 'tieKUM')],
    hiddenimports=[],
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
    name='init_multiple_U',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
