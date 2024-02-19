#! /bin/bash

# This script is used to publish the project to the python package index (pypi)

# copy all json from root to py_countries_states_cities_database
cp *.json py_countries_states_cities_database/

# Remove the previous build
rm -rf dist
python setup.py sdist
twine upload -r testpypi dist/*
twine upload dist/*
