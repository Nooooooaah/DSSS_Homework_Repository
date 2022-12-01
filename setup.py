# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:07:44 2022

@author: noahs
"""

from setuptools import setup

setup(
    name='DSSS_Homework_Repository',
    version='0.1.0',    
    description='A code which creates colorfull snowflakes',
    url='https://github.com/Nooooooaah/DSSS_Homework_Repository.git',
    author='Noah Schäfer',
    author_email='noah.schaefer@fau.de',
    license='Apache License 2.0',
    packages=['snowflake'],
    install_requires=[
                      'numpy'                    
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: DSSS Tutors/ Researchers',
        'License :: Apache License 2.0',  
        'Operating System :: Windows',        
        'Programming Language :: Python :: 3.9',
    ],
)