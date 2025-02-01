from tqdm import tqdm
import time
import ciphers



with open("wordlists/words.txt", 'r') as file:
    words = [line.strip() for line in file]

words = sorted(words, key=len)
realTest = ciphers.realEngine("small_specialized")

total=0
text = "vyc fnweb zghkp wmm ciogq dost kft eobp bdz."


for key in tqdm(words, desc="Processing", unit="item"):
    total+=1

    plaintext = ciphers.vigenere.decrypt(text, key)

    if realTest.plaintext_or_ciphertext(plaintext):
        print(plaintext, key)
        exit()

# I think a larger text is required for kasiski , etc, so doing this would probably be the best method, but increase by letter size (words of length1, 2, 3, etc)