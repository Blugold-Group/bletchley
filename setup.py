from setuptools import setup, find_packages

setup(
    name="bletchley",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "my-cli-tool=my_cli_tool.cli:main",
        ],
    },
)
