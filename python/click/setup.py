from distutils.core import setup

setup(
    name='shell-command',
    version='1.0',
    py_modules=['cmd'],
    install_requires=[
         'Click'
    ],
    entry_points='''
         [console_scripts]
         os=cmd:cli
    ''',
)
