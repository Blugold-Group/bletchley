"""
This file provides access to name-that-hash and search-that-hash, tools which can classify a given hash and do a reverse lookup on it with various databases

"""

import subprocess

def guess(hash):
    subprocess.run(["nth", "-t", hash])

    if input("Do you want to search this hash in online databases? [y/n] ")=="y":
        subprocess.run(["sth", "-t", hash])
