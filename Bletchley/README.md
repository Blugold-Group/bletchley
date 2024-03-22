# Bletchley

A Cryptanalysis Suite 

## Pre-Requisites

All of the required packages are located in requirments.txt

You can install them by running 

```
pip install -r requirements.txt
```

## Overview

Bletchley has a number of tools to aid in cryptanalysis, including

1. Frequency analysis
    - [ ] Frequency analysis displayed in graphs
    - [ ] Automatic decryption using frequency analysis
    
2. Attempted decryption of the following ciphers
    - [x] Caesar
    - [x] Vigenere
    - [x] Rot13
    - [ ] Enigma
    - [x] Atbash
    - [x] Playfair
    - [x] Affine
    - [x] Baconian
    - [ ] Rail-Fence
    - [ ] Substitution Cipher
    - [ ] Columnar Transposition Cipher
    - [ ] Autokey Cipher
    - [ ] Beaufort Cipher
    - [ ] Porta Cipher
    - [ ] Running Key Cipher
    - [ ] Homophonic Substitution Cipher
    - [ ] Four Square Cipher
    - [ ] Hill Cipher
    - [ ] ADFGVX Cipher
    - [ ] ADFGX Cipher
    - [ ] Bifid Cipher
    - [ ] Trifid Cipher
    - [ ] Straddle Checkerboard Cipher 

    Also, common encodings such as 
    - [ ] Base32
    - [ ] Base64
    - [ ] ASCII85

    Can also recognize the following, but likely cannot decrypt them
    - [x] MD5
    - [x] SHA-1
    - [x] RIPEMD-128
    - [x] RIPEMD-160
    - [x] RIPEMD-256
    - [x] RIPEMD-320
    - [x] Whirlpool
    - [x] SHA2-224
    - [x] SHA2-256
    - [x] SHA2-384
    - [x] SHA2-512
    - [x] SHA3-224
    - [x] SHA3-256
    - [x] SHA3-384
    - [x] SHA3-512
    - [x] SHAKE128
    - [x] SHAKE256
    - [x] Keccack

3. A static tool which tests a ciphertext for the above ciphers
    - Uses hardcoded values with distinct characteristics of ciphertexts goven by these algorithms
  
4. Case transformers (upper to lowercase and vice versa)

And the crown jewel 

5. A dynamic tool built on machine learning which analyses ciphertext and gives best guesses as to what the cipher is and what steps can be taken to decrypt the ciphertext

The power givin by this repo is the ability to string various "departments" (tools) together, creating a dynamic solution finding tool. 

Find what the plaintexts are likely to be, probably mostly quotes from GoodReads or something. 

Encrypt lots of plaintexts with various algorithms, and ML it to detect what cipher was used

## Description of wordlists

The specialized wordlists have been modified to perform better 

quotes.txt - A file given by DOI:10.13140/RG.2.1.4386.4561 (10.8MB)
words_dictionary.json - A json-izes version of quotes.csv (6.8 MB)
words.txt - A file of the top 20000 most commonly used elgish words (155.4 kB)
dictionary.txt - The lowercase verion of https://pypi.org/project/english-dictionary/ (1.2 MB)
words_dictionary_specialized.txt - words_dictionary.json except all words with less than 4 charcaters and which aren't in dictionary.txt are removed (1.0 MB)
testquotes.txt - Quotes which aren't included in quotes.txt, used for testing accuracy

## Sources

Madadipouya, Kasra. (2016). CSV dataset of 76,000 quotes, suitable for quotes recommender systems or other analysis.. 10.13140/RG.2.1.4386.4561. 

english_dictionary (used for dictionary.txt) : https://pypi.org/project/english-dictionary/ Created by Daniel Delluomo 