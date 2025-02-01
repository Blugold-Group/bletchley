"""
This file provides access to name-that-hash and search-that-hash, tools which can classify a given hash and do a reverse lookup on it with various databases

"""

import subprocess

def guess(hash):
    subprocess.run(["nth", "-t", hash])