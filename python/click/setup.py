from distutils.core import setup

setup(
    name='Numberworld',
    version='1.0',
    py_modules=['number'],
    install_requires=[
         'Click'
    ],
    entry_points='''
         [console_scripts]
         os=number:cli
    ''',
)
