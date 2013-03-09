from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

setup(windows=['game_of_life_cell.py'], 
	data_files=[('.', ['libiomp5md.dll']),],
    options = {
        'py2exe': {
            'includes': ['ctypes', 'logging'],
            'excludes': ['OpenGL']
        }
    }
)