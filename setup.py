from importlib.metadata import entry_points
from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Script for sorting entire files in selected folder',
    url='http://github.com/SerhioKAS/Go_IT9_Kashpurenko_HW_7',
    author='Kashpurenko',
    author_email='sarhiokas@gmail.com',
    license='MIT',
    platforms='windows, unix',
    packages=find_namespace_packages(),
    entry_points={'console_scripts' : ['cleanfolder = clean_folder.clean: start_func']}
)