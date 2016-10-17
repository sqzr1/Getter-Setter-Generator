"""
  This is the py2exe Setup file. This file is used to create an
  executable of the program using py2exe.
"""


from distutils.core import setup
import py2exe
 
setup(
    windows=['gsg/run.py'],
    options = {
        'py2exe': {
            'packages': ['controller']
        }
    }
)
