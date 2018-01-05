#! /usr/bin/env python
#
# Copyright (C) 2018 Mikko Kotila


DESCRIPTION = "Tibetan Language Workbench"
LONG_DESCRIPTION = """\
bö (tib. བོད་) means Tibet, and ke (tib. སྐད) means language,
so together böke means Tibetan Language. bokepy is a shorthand
for boke and python, and is a Tibetan Language Processing Library
built for handling the most common language processing tasks in a
straightforward way. Bokepy is built from the ground up to facilitate
for a wide range of research challenges, including those far beyond the
scope of typical scholarly interest. This includes rapid testing of ideas
and prototyping of completely new technology solutions.
"""

DISTNAME = 'bokepy'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'https://github.com/mikkokotila/bokepy'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/mikkokotila/bokepy.git'
VERSION = '0.1'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

def check_dependencies():

    install_requires = []

    try:
        import pandas
    except ImportError:
        install_requires.append('pandas')

    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=['bokepy',
                    'bokepy.grapheme'],

          classifiers=[
                     'Intended Audience :: Science/Research',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 2.7',
                     'License :: OSI Approved :: MIT License',
                     'Topic :: Scientific/Engineering :: Human Machine Interfaces',
                     'Topic :: Scientific/Engineering :: Artificial Intelligence',
                     'Topic :: Scientific/Engineering :: Linguistics',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'])
