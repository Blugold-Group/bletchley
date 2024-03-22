import joblib
from sklearn.feature_extraction.text import CountVectorizer
import ciphers

global classifier
global vectorizer

classifier = joblib.load('Bletchley/large_cipher_classifier_model.pkl')
with open('Bletchley/large_count_vectorizer.pkl', 'rb') as f:
    vectorizer = joblib.load(f)

def predict_cipher(ciphertext):
    global classifier
    global vectorizer

    ciphertext_vector = vectorizer.transform([ciphertext])

    predicted_cipher = classifier.predict(ciphertext_vector)

    return predicted_cipher[0]


q=open("Bletchley/wordlists/testquotes.txt", "r")
quotes=q.read().splitlines()
q.close()
total=len(quotes)
correct=0
incorrect=0

#a: vigenere
#b: caesar
#c: baconian
#d: atbash
#e: affine

acorrect=0
bcorrect=0
ccorrect=0
dcorrect=0
ecorrect=0

for quote in quotes:
    v = ciphers.vigenere(quote)
    c = ciphers.caesar(quote)
    b = ciphers.baconian(quote)
    at = ciphers.atbash(quote)
    af = ciphers.affine(quote)

    # Predict the cipher used
    if predict_cipher(v) == "vigenere":
        correct+=1
        acorrect+=1
    else:
        incorrect+=1
        print("vigenere predicted as", predict_cipher(v))

    if predict_cipher(c) == "caesar":
        correct+=1
        bcorrect+=1
    else:
        incorrect+=1
        print("caesar predicted as", predict_cipher(c))

    if predict_cipher(b) == "baconian":
        correct+=1
        ccorrect+=1
    else:
        incorrect+=1
        print("baconian predicted as", predict_cipher(b))

    if predict_cipher(at) == "atbash":
        correct+=1
        dcorrect+=1
    else:
        incorrect+=1
        print("atbash predicted as", predict_cipher(at))

    if predict_cipher(af) == "affine":
        correct+=1
        ecorrect+=1
    else:
        incorrect+=1
        print("affine predicted as", predict_cipher(af))

        

print("Correct: :", correct)
print("Incorrect: :", incorrect)

print("Vigenere detection rate:  "+str(acorrect/total*100)+"%")
print("Caesar detection rate:  "+str(bcorrect/total*100)+"%")
print("Baconian detection rate:  "+str(ccorrect/total*100)+"%")
print("Atbash detection rate:  "+str(dcorrect/total*100)+"%")
print("Affine detection rate:  "+str(ecorrect/total*100)+"%")

print("Overall accuracy rate:  "+str(correct/total*100/5)+"%")