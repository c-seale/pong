import cx_Freeze

cx_Freeze.setup(
    name='cseale\'s Pong!',
    version='0.1',
    options={'build_exe': {'packages': [], 'include_files': []}},
    executables=[cx_Freeze.Executable('main.py', base='Win32GUI')]
)
