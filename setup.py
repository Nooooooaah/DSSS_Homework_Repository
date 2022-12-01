# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:07:44 2022

@author: noahs
"""

from setuptools import find_packages
from distutils.core import setup

setup(
    name='snowflake',
    version='0.1.0',    
    description='A code which creates colorfull snowflakes',
    url='https://github.com/Nooooooaah/DSSS_Homework_Repository.git',
    author='Noah Schäfer',
    author_email='noah.schaefer@fau.de',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=['numpy', 'turtel'    ],   
)