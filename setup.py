from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Simple flask web dev kit'
LONG_DESCRIPTION = 'A package that allows to simplify the process of building web apps with flask.'

# Setting up
setup(
    name="pywebdark",
    version=VERSION,
    author="Borat Baka",
    author_email="<edmachine@tutanota.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['flask'],
    keywords=['python', 'sockets', "flask", "web dev"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)