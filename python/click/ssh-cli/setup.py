from distutils.core import setup

setup(
    name='Server-cli',
    version='1.0',
    py_modules=['auth'],
    install_requires=[
         'Click'
    ],
    entry_points='''
         [console_scripts]
         servercmd=auth:cli
    ''',
)
