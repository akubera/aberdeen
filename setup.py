#!/usr/bin/env python
#
# setup.py
#
"""Aberdeen Setup Script"""

from setuptools import setup, find_packages
from importlib.machinery import SourceFileLoader

desc = "Conversion from markdown files to database entries to use as the backend of a blog"


NAME = "aberdeen"

CONSOLE_SCRIPTS = [
    'aberdeen-init = aberdeen.cli.init:main',
    'aberdeen-update-hook = aberdeen.cli.update_hook:main'
]

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
    "Programming Language :: Python :: 3.6",
    "Topic :: Utilities",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "License :: OSI Approved :: Apache Software License"
]


meta = SourceFileLoader("meta", "aberdeen/__meta__.py").load_module()

tar_url = 'https://github.com/akubera/aberdeen/archive/v%s.tar.gz' % (meta.version)


setup(
    name=NAME,
    packages=find_packages(exclude=['test']),
    version=meta.version,
    description=desc,
    url=meta.url,
    download_url=tar_url,
    author=meta.author,
    author_email=meta.author_email,
    keywords=KEYWORDS,
    license=meta.license,
    classifiers=CLASSIFIERS,
    platforms='any',
    install_requires=REQUIRES,
    extras_require=OPTIONAL_REQUIRES,
    entry_points={
        'console_scripts': CONSOLE_SCRIPTS,
    },
    package_data={'aberdeen': ['git_hooks/*']}
)
