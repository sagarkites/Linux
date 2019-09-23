from distutils.core import setup

setup(
    name='Regular-expcli',
    version='1.0',
    py_modules=['reg'],
    install_requires=[
         'Click'
    ],
    entry_points='''
         [console_scripts]
         regcli=reg:cli
    ''',
)
