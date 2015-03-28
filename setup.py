#
# setup.py
#
"""Aberdeen Setup Script"""

from setuptools import setup
import aberdeen

desc = "Conversion from markdown files to database entries to use as the backend of a blog"

REQUIRES = [
    'emoji',
    'termcolor2'
]

OPTIONAL_REQUIRES = {
    'markdown': ['Markdown'],
    'mongodb': ['pymongo','asyncio_mongo']
}

KEYWORDS = [
    'markdown',
    'blog',
    'nosql',
    'mongodb'
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

setup(
    name="aberdeen",
    packages=["aberdeen"],
    version=aberdeen.__version__,
    description=desc,
    url=aberdeen.__homepage__,
    author=aberdeen.__author__,
    author_email=aberdeen.__contact__,
    keywords=KEYWORDS,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    install_requires=REQUIRES,
    extras_require=OPTIONAL_REQUIRES,
    scripts=['scripts/aberdeen-init'],
    package_data={'aberdeen': ['git_hooks/*']}
)
