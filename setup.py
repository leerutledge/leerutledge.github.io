"""SplitCalculator python package configuration."""

from setuptools import setup

setup(
    name='splitCalculator',
    version='0.1.0',
    packages=['splitCalculator'],
    include_package_data=True,
    install_requires=[
        'Flask==1.0',
        'arrow==0.10.0',
        'sh==1.12.14',
    ],
)