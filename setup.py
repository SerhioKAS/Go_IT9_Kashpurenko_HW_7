from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name='Clean Folder',
    version='1.0.0',
    description='Code sorts entire files from selected folder',
    url='https://...',
    author='Kashpurenko S.M.',
    packages=find_packages(),
    entry_points={'complete_scripts': ['clean_folder: clean_folder.clean : main']}
)