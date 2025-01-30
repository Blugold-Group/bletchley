from setuptools import setup, find_packages

setup(
    name="bletchley",
    version="0.5.0",
    url='https://github.com/ThisIsNotANamepng/bletchley',
    long_description=open('README.md').read(),
    description="A cryptography suite",
    long_description_content_type='text/markdown',
    author='The Blugold Group',
    license="MPL-2.0",
    packages=find_packages(),
    install_requires=['bs4', 'search-that-hash', 'Faker', 'Brotli', 'colorama', 'name-that-hash', 'plotext', 'pyenigma', 'base58'],
    entry_points={
        "console_scripts": [
            "bletchley=bletchley.cli:main",
        ],
    },
)