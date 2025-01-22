from setuptools import setup, find_packages

setup(
    name="bletchley",
    version="0.4.0",
    url='https://github.com/ThisIsNotANamepng/bletchley',
    long_description=open('README.md').read(),
    description="A cryptography suite",
    long_description_content_type='text/markdown',
    author='The Blugold Group',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bletchley=bletchley.cli:main",
        ],
    },
)