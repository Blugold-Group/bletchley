import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import ciphers
import time
import joblib

exported_model_name="Bletchley/cipher_classifier_model.pkl"
exported_vectorizer_name="Bletchley/count_vectorizer.pkl"

start=time.time()
# Sample dataset (ciphertext samples with corresponding cipher labels)
ciphertext_samples = []

print("Reading and appending data...")
q=open("Bletchley/wordlists/large_quotes.txt", "r")
quotes=q.read().splitlines()
q.close()

for i in quotes:
    ciphertext_samples.append((ciphers.vigenere(i), "vigenere"))
    ciphertext_samples.append((ciphers.caesar(i), "caesar"))
    ciphertext_samples.append((ciphers.baconian(i), "baconian"))
    ciphertext_samples.append((ciphers.atbash(i), "atbash"))
    ciphertext_samples.append((ciphers.affine(i), "affine"))



print("Splitting...")
# Split data into ciphertext and corresponding labels
ciphertexts, labels = zip(*ciphertext_samples)

print("Extracting data...")
# Feature extraction (character n-grams)
vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 2))
X = vectorizer.fit_transform(ciphertexts)

print("Training the classifier...")
# Train a Random Forest classifier
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X, labels)

print("Exporting the model")
joblib.dump(classifier, exported_model_name)
joblib.dump(vectorizer, exported_vectorizer_name)

print("Model trained and exported to '"+exported_model_name+"'")

print("Time taken:  "+str(time.time()-start))
