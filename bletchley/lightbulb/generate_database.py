import random
import csv
from faker import Faker

# Use faker to get words for the key and sentences for the plaintext
fake = Faker()

# The number of examples to generate
NUM_EXAMPLES = 1000

def random_caesar_cipher():
    sentence = fake.sentence()
    
    key = random.randint(1, 25)
    
    encrypted_sentence = ""
    for char in sentence:
        if char.isalpha():
            shift = key if char.islower() else key
            new_char = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a')) if char.islower() else \
                       chr(((ord(char.upper()) - ord('A') + shift) % 26) + ord('A'))
            encrypted_sentence += new_char
        else:
            encrypted_sentence += char
    
    return encrypted_sentence

def random_atbash_cipher():
    sentence = fake.sentence()
    
    encrypted_sentence = ""
    for char in sentence:
        if char.isalpha():
            if char.islower():
                encrypted_sentence += chr(219 - ord(char))  # 'a' + 'z' = 219
            else:
                encrypted_sentence += chr(155 - ord(char))  # 'A' + 'Z' = 155
        else:
            encrypted_sentence += char
    
    return encrypted_sentence

def generate_cipher_examples(num_examples):
    with open('ciphertext_dataset.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Encrypted Sentence', 'Cipher Used'])  # CSV header

        for _ in range(num_examples):
            # Randomly choose cipher
            if random.choice([True, False]):
                encrypted_sentence = random_caesar_cipher()
                cipher_used = 'Caesar'
            else:
                encrypted_sentence = random_atbash_cipher()
                cipher_used = 'Atbash'
            
            # Write encrypted sentence and cipher type to CSV
            writer.writerow([encrypted_sentence, cipher_used])

    print(f"CSV file 'ciphertext_dataset.csv' with {num_examples} examples has been created.")


generate_cipher_examples(NUM_EXAMPLES)
