# Lightbulb

Lightbulb is the ML classical cipher detection engine

It is built off of previous academic work

## Ciphers

Some classical ciphers can be broken in less than a second with computers, so we exclude those from the model. The ciphers we inlcude are

- Vigenere
- Affine

We measure the following statistics about a ciphertext

- Letter frequencies
- Trigram frequencies
- Entropy
- Character variance
- Chi squared
- Index of coincidence


** Use this - http://practicalcryptography.com/cryptanalysis/text-characterisation/identifying-unknown-ciphers/ **

https://web.archive.org/web/20120108030145/http://home.comcast.net/~acabion/acarefstats.html used the following stats

IC is the Index of Coincidence multiplied by 1000.
MIC is the maximum Index of Coincidence for periods 1-15, multiplied by 1000.
MKA is the maximum kappa value for periods 1-15 , multiplied by 1000.
DIC is the Digraphic Index of Coincidence, multiplied by 10,000.
EDI is the Digraphic IC for even-numbered pairs, multiplied by 10,000.
LR is the square root of the percentage of 3 symbol repeats, multiplied by 1000.
ROD is the percentage of odd-spaced repeats to all repeats.LDI is AAHJU’s average log-digraph score.
SDD is the average Single letter-Digraph Discrepancy score. 
















http://dx.doi.org/10.3384/ecp183164 uses 27 characteristics of a ciphertext to train the model, those being

removing (HAS_0, HAS_H, HAS_J, HAS_X)

- Average Single Letter – Digraph Discrepancy Score (SDD) 
- Chi Square (CHI2)
- Digraphic Index of Coincidence (DIC)
- Double Letter (DBL)
- Estimated Auto Correlation (AUTO)
- Frequencies (FRQ)
- Has Space (HAS_SP)
- Index of Coincidence (IoC)
- Log Digraph Score (LDI)
- Log Digraph Score for Autokey, Beaufort, Porta, Slidefair, Vigenere, and Portax (A_LDI, B_LDI, P_LDI, S_LDI, V_LDI, PTX)
- Long Repeat (LR)
- Max Bifid DIC for Periods 3-15 (BDI)
- Max Columnar SDD Score for Periods 4-15 (CDD)
- Max Kappa (MKA)
- Max Nicodemus IC (NIC)
- Max STD Score for Swagman Periods 4-8 (SSTD)
- Maximum Index of Coincidence (MIC)
- Normal Order (NOMOR)
- Phillips IC (PHIC)
- Repetition Feature (REP)
- Repetition Odd (ROD)
- Reverse Log Digraph (RDI)
- Shannon’s Entropy Equation (SHAN)

## Datasets

- romeo.txt - Plaintext Romeo and Juliet play script and stage direction (https://folger-main-site-assets.s3.amazonaws.com/uploads/2022/11/romeo-and-juliet_TXT_FolgerShakespeare.txt)
- movie_lines.txt - The dialogue lines from the Cornell Movie Dialoues Corpus (https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)


## Resources

TO further understand this field and problem, consider the following sources

- US Army cryptanalysis field guide - https://irp.fas.org/doddir/army/fm34-40-2/
