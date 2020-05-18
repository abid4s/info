#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Info - Email OSINT
# @url    : http://github.com/Abi4s
# @author : Muhammad Abid (xKILLERDEADx)

from setuptools import setup 

setup(
    name='infoga',

    version='0.1.5',
    description='Email OSINT',
    url='https://github.com/Abi4s',
    
    author = 'M Abid (xKILLERDEADx) Outaadi',
    author_email='xbrute@protonmail.ch',
    license='GPLv3',

    install_requires = ['colorama','requests','urllib3'],
    console =['info.py'],
)