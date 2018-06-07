#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='Chlikelihood',
    version='0.0.2',
    description=(
        '用于比较两个中文句子相似度的工具'
    ),
    long_description=open('README.md').read(),
    author='ZhanPw',
    author_email='zhanpw97@gmail.com',
    license='MIT License',
    packages=find_packages(),
    install_requires=['jieba'],
    platforms=["all"],
    url='https://github.com/ZhanPwBibiBibi/CHlikelihood',
)