#!/usr/bin/env python3
# coding:utf-8

from setuptools import setup

setup(name='fcpy',
      version='0.0.1',
      description='For predicting japanase stocks.',
      author='Mogu',
      author_email='kbu94984@gmail.com',
      url='',
      packages=['src','src/core'],
      install_requires=[],
      entry_points="""
      [console_scripts]
      fcpy = fcpy:__main__
      """,
)

