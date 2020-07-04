import os

import cx_Freeze

SOUND_DIRECTORY = 'sound'
SOUND_FILES = [os.path.join(SOUND_DIRECTORY, f) for f in os.listdir(SOUND_DIRECTORY) if
               os.path.isfile(os.path.join(SOUND_DIRECTORY, f))]
SOUND_INCLUDES = [(sf, sf) for sf in SOUND_FILES]

cx_Freeze.setup(
    name='cseale\'s Pong!',
    version='0.1',
    options={
        'build_exe': {
            'packages': [],
            'include_files': [] + SOUND_INCLUDES
        }
    },
    executables=[cx_Freeze.Executable('main.py', base='Win32GUI')]
)
