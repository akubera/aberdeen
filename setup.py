#
# setup.py
#
"""Aberdeen Setup Script"""

from setuptools import setup
import aberdeen
REQUIRES = [

]

OPTIONAL_REQUIRES = {
    'markdown': ['Markdown'],
    'mongodb': ['asyncio_mongo']
}

KEYWORDS = [
    'markdown',
    'blog',
    'nosql',
    'mongodb'
]

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    'Topic :: Utilities',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
]

setup(
    name="aberdeen",
    packages=["aberdeen"],
    version=aberdeen.__version__,
    description="Conversion from markdown files to database tables for a blog",
    author=aberdeen.__author__,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    install_requires=REQUIRES,
    extras_require=OPTIONAL_REQUIRES
)
