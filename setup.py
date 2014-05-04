from setuptools import setup, find_packages

from cotd import __version__

setup(
    name='conman',
    version=__version__,
    author='Scott Griffin',
    author_email='scott@scottgriffin.net',
    packages=find_packages( exclude=['tests'] ),
    description='Module that loads multiple config types including raw python files.',
    long_description=open('README.md').read(),
)
