from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import joblib
import ciphers
import time
import random

texts = []
labels = []
answers = []


start=time.time()

print("Adding encrypted values... ")

f=open("wordlists/quotes.csv", "r")
quotes=f.readlines()
f.close()

rounds=10
for j in range(1,rounds+1):
    print("Round "+str(j)+" out of "+str(rounds)+" complete")

    for i in quotes:
        data=ciphers.caesar(i)
        texts.append(data)
        labels.append("caesar")
        data=ciphers.vigenere(i)
        texts.append(data)
        labels.append("vigenere")


print("Training... ")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Training a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_tfidf, y_train)

# Exprting the vectorization and classification models
joblib.dump(clf, 'naive_bayes_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

# Predictions
predictions = clf.predict(X_test_tfidf)

"""
# Classification of new strings
new_texts = []
i=0
while (i<100):
    new_texts.append(vigenere.randomText())
    answers.append("random")
    i+=1
i=0
while (i<100):
    new_texts.append(vigenere.ciphertext())
    answers.append("cipher")
    i+=1

"""

end=time.time()
print("Time taken  :  ", end-start)

new_texts=[]
test="s"

"""
while test!= "":
    test=input("What do you want to test? [exit]   ")
    new_texts.append(test)
    ans=input("c/v?   ")
    if ans=="v":
        answers.append("vigenere")
    else:
        answers.append("caesar")
"""

print("Running test cases... ")

test_caesar_quotes=[]
test_vigenere_quotes=[]

testCases=10
for i in range(testCases//2):
    test_caesar_quotes.append(ciphers.caesar(random.choice(quotes)))
for i in range(testCases//2):
    test_vigenere_quotes.append(ciphers.vigenere(random.choice(quotes)))

for i in test_caesar_quotes:
    print("Added to caesar list")
    new_texts.append(i)
    answers.append("caesar")
for i in test_vigenere_quotes:
    print("Added to vigenere list")
    new_texts.append(i)
    answers.append("vigenere")

# Vectorize the new texts using the same TF-IDF vectorizer
new_texts_tfidf = vectorizer.transform(new_texts)

# Predict
new_predictions = clf.predict(new_texts_tfidf)

correct=0
incorrect=0
a="caesar"
b="vigenere"

aPredictedAsa=0
aPredictedAsb=0
bPredictedAsa=0
bPredictedAsb=0

for text, prediction, answer in zip(new_texts, new_predictions, answers):
    if prediction==answer:
        correct+=1
        if prediction==a:
            aPredictedAsa+=1
        else:
            bPredictedAsb+=1
    else:
        incorrect+=1
        if prediction==b:
            bPredictedAsa+=1
        else:
            aPredictedAsb+=1
    
print("Correct: ", str(correct) + " ("+str(correct/(incorrect+correct)*100)[0:5]+"%),   Incorrect: ", str(incorrect)+ " ("+str(incorrect/(incorrect+correct)*100)[0:5]+"%)")
print(a+" predicted as "+a+": ", aPredictedAsa)
print(a+" predicted as "+b+": ", aPredictedAsb)
print(b+" predicted as "+a+": ", bPredictedAsa)
print(b+" predicted as "+b+": ", bPredictedAsb)
