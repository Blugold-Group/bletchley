# Development

This document outlines how the code is laid out and how it works in order to lower the barrier of entry for new developers.

### Terminology

'key' and 'password' are interchangeable, both meaning a secret used to encrypt/decrypt a text

'pipe in' = 'pass'

## Architecture

Bletchley is designed to be a python package, available from the cli and in python scripts through a library.

There are metadata files (readme.md, development.md, requirements.txt, license, etc.) in the root of the directory

As with most python packages, the code for the main program in the `/bletchley` folder

### /bletchley/cli.py

cli.py is the file which handles the cli (command line interface) interface. It's split up into two part.

#### main()

The main() function runs when the file is run. It processes cli input using the standard [argparse](https://docs.python.org/3/library/argparse.html) library. `args = parser.parse_args()` captures all of the flag passed through the cli, any errors in syntax and stuff is handled by argparse based on the rules created with things like

```
encryption_parser = subparsers.add_parser("encrypt", help="Encrypt a text.")
encryption_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
encryption_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to encrypt the text with")
encryption_parser.add_argument("-p", "--password", type=str, required=False, help="The password to encrypt the text with")
```

From there, it classifies the command with a series of if statements, and passes the requisite data to the other functions as necessary

#### Other functions

The other functions (all of them that aren't main()) provide a high level interface for the rest of the library.

The functions `check_text_password`, `check_password_not_needed`, and `convert_num_password` provide utilities to prepare text input from the cli. They check whether that the password passed is a text (some ciphers need a text password), warns if a password was passed and wasn't required, and tries to convert the string password input to an integer (because some ciphers require int passwords). These are used as needed for different ciphers to provide standard errors and warning across the tool

### /bletchley/ciphers.py

Is the core file for cryptographic primitives. It includes the code for encryption and decryption of difference ciphers. Each cipher has is a class which has `about()`, `encrypt()`, `decrypt()` and whatever else it needs internally to function.

### /bletchley/bruteforce.py

### /bletchley/encodings.py

Provides functions for different encodings

### /bletchley/start.py

While other files provide unbiased, highly customizable functions to do whatever the user wants in an extensible way, start.py provides the `run()` function. The `run()` function takes a ciphertext and runs through checks to automatically decrypt the text without knowing the cipher or key. It takes very few options, instead running an opinionated checklist. It aims to do everything automatically, allowing the user to pipe any ciphertext into it and get a response quickly using high-level cryptographic methods written by club cryptographers

### /bletchley/frequency.py

The `frequency.py` file provides the tools for frequency analysis. It lets the user pass a text and get either raw data or charts of the frequencies for different characters

### /bletchley/recognizeHash.py

Provides access to the `name-that-hash` and `search-that-hash` libraries, which classify hashes and searches them in online databases (`search-that-hash doesn't work well, might remove in the future`)

### /bletchley/stats.py

Provides functions for the statistical measurements of a passed text

## Program Workflow

The workflow for running the program is as follows:

cli

library


### ML Aided Ciphertext Classification
