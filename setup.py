# Setup script for the pybmp package
#
# Usage: python setup.py install
#
import os
from setuptools import setup, find_packages

def getDataFiles(submodule, folder):
    datadir = os.path.join('wqio', submodule, folder)
    files = [d for d in map(
        lambda x: os.path.join(datadir, x),
        os.listdir(datadir)
    )]
    return files


DESCRIPTION = "wqio: Water Quality Inflow/Outflow"
LONG_DESCRIPTION = DESCRIPTION
NAME = "wqio"
VERSION = "0.1"
AUTHOR = "Paul Hobson (Geosyntec Consultants)"
AUTHOR_EMAIL = "phobson@geosyntec.com"
URL = "https://github.com/Geosyntec/wqio"
DOWNLOAD_URL = "https://github.com/Geosyntec/wqio/archive/master.zip"
LICENSE = "BSD 3-clause"
PACKAGES = find_packages()
PLATFORMS = "Python 2.7, 3.3 and later."
CLASSIFIERS = [
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Intended Audience :: Science/Research",
    "Topic :: Formats and Protocols :: Data Formats",
    "Topic :: Scientific/Engineering :: Earth Sciences",
    "Topic :: Software Development :: Libraries :: Python Modules",
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
]
INSTALL_REQUIRES = ['seaborn']
PACKAGE_DATA = {}
DATA_FILES = [
    ('wqio_data/testing', getDataFiles('testing', 'data')),
]

if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        download_url=DOWNLOAD_URL,
        license=LICENSE,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        data_files=DATA_FILES,
        platforms=PLATFORMS,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
    )
