import joblib

def predict_cipher(ciphertext):
    classifier = joblib.load('Bletchley/large_cipher_classifier_model.pkl')
    with open('Bletchley/large_count_vectorizer.pkl', 'rb') as f:
        vectorizer = joblib.load(f)

    ciphertext_vector = vectorizer.transform([ciphertext])

    predicted_cipher = classifier.predict(ciphertext_vector)

    return predicted_cipher[0]

