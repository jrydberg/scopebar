"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

setup(
    name="ScopeBarExample",
    app=["main.py"],
    data_files=["ScopeBarExample.nib"],
    packages=["MGScopeBar"],
    options=dict(py2app=dict(
            plist="ScopeBarExample.plist",
            )),
)
