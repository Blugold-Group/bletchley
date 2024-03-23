import joblib

def predict_cipher(ciphertext):
    classifier = joblib.load('Bletchley/cipher_classifier_model.pkl')
    with open('Bletchley/count_vectorizer.pkl', 'rb') as f:
        vectorizer = joblib.load(f)

    ciphertext_vector = vectorizer.transform([ciphertext])

    predicted_cipher = classifier.predict(ciphertext_vector)

    return predicted_cipher[0]

