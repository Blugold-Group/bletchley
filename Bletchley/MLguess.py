from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import joblib
import ciphers
import time

texts = []
labels = []
answers = []


start=time.time()

ciphers.vigenere()

end=time.time()
print("Time taken  :  ", end-start)

input("  -------   Stop Here   -------  ")
for i in range(10000):
    data=vigenere.randomData()

    texts.append(data[0])
    labels.append("cipher")
    texts.append(data[1])
    labels.append("random")

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

# Vectorize the new texts using the same TF-IDF vectorizer
new_texts_tfidf = vectorizer.transform(new_texts)

# Predict
new_predictions = clf.predict(new_texts_tfidf)

correct=0
incorrect=0
cipherPredictedAsRandom=0
randomPredictedAsCipher=0
cipherPredictedAsCipher=0
randomPredictedAsRandom=0

for text, prediction, answer in zip(new_texts, new_predictions, answers):
    if prediction==answer:
        correct+=1
        if prediction=="cipher":
            cipherPredictedAsCipher+=1
        else:
            randomPredictedAsRandom+=1
    else:
        incorrect+=1
        if prediction=="cipher":
            randomPredictedAsCipher+=1
        else:
            cipherPredictedAsRandom+=1
    
print("Correct: ", str(correct) + " ("+str(correct/(incorrect+correct)*100)[0:5]+"%),   Incorrect: ", str(incorrect)+ " ("+str(incorrect/(incorrect+correct)*100)[0:5]+"%)")
print("Cipher predicted as cipher: ", cipherPredictedAsCipher)
print("Random predicted as random: ", randomPredictedAsRandom)
print("Cipher predicted as random: ", cipherPredictedAsRandom)
print("Random predicted as Cipher: ", randomPredictedAsCipher)
"""