from setuptools import setup, find_packages

setup(

    name='setuppackage',
    version='1.0.0',
    packages=find_packages(exclude=['*tests*']),
)
