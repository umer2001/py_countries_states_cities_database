from setuptools import setup, find_packages
import glob

long_description = open("README.md", "r", encoding="utf-8").read()

setup(
    name="py_countries_states_cities_database",
    version="2.2.1",
    description="A Python package to get countries, states and cities information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    data_files=[
        ("py_countries_states_cities_database", glob.glob("./*.json")),
    ],
    packages=find_packages(),
    url="https://github.com/umer2001/py_countries_states_cities_database",
    author="Umer Farooq",
    author_email="umer2001.uf@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="countries states cities database",
    extras_require={
        "dev": [
            "black",
            "twine",
            "wheel",
        ],
    },
)
