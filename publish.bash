#! /bin/bash

# This script is used to publish the project to the python package index (pypi)

# Remove the previous build
rm -rf dist
python setup.py sdist
twine upload -r testpypi dist/*
twine upload dist/*
