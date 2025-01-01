# Bletchley

Bletchley has a number of tools to aid in cryptanalysis, including

1. Frequency analysis
    - [ ] Frequency analysis displayed in graphs
    - [ ] Automatic decryption using frequency analysis
    
2. Attempted automated decryption of the following ciphers
    - [x] Caesar
    - [x] Vigenere
    - [x] Rot13
    - [ ] Enigma
    - [x] Atbash
    - [x] Playfair
    - [x] Affine
    - [x] Baconian
    - [x] Rail-Fence
    - [ ] Substitution
    - [ ] Columnar Transposition
    - [ ] Autokey
    - [ ] Beaufort
    - [ ] Porta
    - [ ] Running Key
    - [ ] Homophonic Substitution
    - [ ] Four Square
    - [ ] Hill
    - [ ] ADFGVX
    - [ ] ADFGX
    - [ ] Bifid
    - [ ] Trifid
    - [ ] Straddle Checkerboard 

    Also, common encodings such as 
    - [ ] Base32
    - [ ] Base64
    - [ ] ASCII85

3. A tool to determine which algorithm was used to make a hash, and a tool to search that hash in various online databases

And the crown jewel 

4. A dynamic tool using machine learning to guess what cipher was used to encrypt a ciphertext, called lightbulb 

Works with the following ciphers
   
     - [x] Vigenere
     - [x] Atbash
     - [x] Baconian


The power given by this repo is the ability to string various "departments" (tools) together, creating a dynamic solution finding tool. 

## Architecture

### ML Aided Ciphertext Classification

### Description of word lists

The specialized word lists have been modified to perform better in this context

* small_quotes.txt - A file given by DOI:10.13140/RG.2.1.4386.4561 (10.8MB)
* large_quotes.txt - A file adapted from kaggle.com/datasets/manann/quotes-500k
* words_dictionary.json - A json-izes version of quotes.csv (6.8 MB)
* words.txt - A file of the top 20000 most commonly used english words (155.4 kB)
* dictionary.txt - The lowercase version of https://pypi.org/project/english-dictionary/ (1.2 MB)
* words_dictionary_specialized.txt - words_dictionary.json except all words with less than 4 characters and which aren't in dictionary.txt are removed (1.0 MB)

### Sources

Madadipouya, Kasra. (2016). CSV dataset of 76,000 quotes, suitable for quotes recommender systems or other analysis.. 10.13140/RG.2.1.4386.4561. 

english_dictionary (used for dictionary.txt) : https://pypi.org/project/english-dictionary/ Created by Daniel Delluomo 