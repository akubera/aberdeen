#!/usr/bin/env python
#
# setup.py
#
"""Aberdeen Setup Script"""

from setuptools import setup, find_packages
from importlib.machinery import SourceFileLoader

desc = "Conversion from markdown files to database entries to use as the backend of a blog"

REQUIRES = [
    'emoji',
    'termcolor2',
    'python-dateutil',
]

OPTIONAL_REQUIRES = {
    'markdown': ['Markdown'],
    'mongodb': ['pymongo','asyncio_mongo']
}

KEYWORDS = [
    'markdown',
    'blog',
    'publishing',
    'nosql',
    'mongodb',
]

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Utilities",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "License :: OSI Approved :: Apache Software License"
]

LICENSE = 'Apache 2.0'

meta = SourceFileLoader("meta", "aberdeen/__meta__.py").load_module()

tar_url = 'https://github.com/akubera/aberdeen/archive/v%s.tar.gz' % (meta.version)


setup(
    name="aberdeen",
    packages=find_packages(exclude=['test']),
    version=meta.version,
    description=desc,
    url=meta.url,
    download_url=tar_url,
    author=meta.author,
    author_email=meta.author_email,
    keywords=KEYWORDS,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    platforms='any',
    install_requires=REQUIRES,
    extras_require=OPTIONAL_REQUIRES,
    scripts=['scripts/aberdeen-init', 'scripts/aberdeen-update-hook'],
    package_data={'aberdeen': ['git_hooks/*']}
)
