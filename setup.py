from setuptools import setup, find_packages
import os
import urllib.request

def download_rockyou():
    # rockyou.txt is helpful, it's too large to be kept in the github repo so we download it to wordlists/ post install

    target_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bletchley', 'wordlists')

    file_url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
    file_path = os.path.join(target_dir, "rockyou.txt")

    # If the file does not exist, download it
    if not os.path.exists(file_path):
        print(f"Downloading rockyou.txt to {file_path}...")
        urllib.request.urlretrieve(file_url, file_path)
        print(f"File downloaded to {file_path}")
    else:
        print("rockyou.txt already downloaded")

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

if __name__ == "__main__":
    download_rockyou()