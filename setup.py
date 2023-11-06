# Always prefer setuptools over distutils
from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="nosql-common",
    version="0.1.0",
    description="Common NOSQL functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0xCoderJoe/nosql-common",
    author="Joe Fasulo",
    author_email="xCoderJoe@proton.me",
    license="Apache 2",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache 2.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["nosql_common"],
    include_package_data=True,
    install_requires=["ibmcloudant",
                      "ibm_cloud_sdk_core",
                      "python-dotenv",
                      "pytest"]
)