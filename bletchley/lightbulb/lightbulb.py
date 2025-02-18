"""
Unified Ciphertext Classification Script

This script can either:
  1. Train a ciphertext classifier from a CSV dataset (using the 'train' subcommand), or
  2. Predict the cipher used for a given ciphertext (using the 'predict' subcommand).

The CSV dataset should have at least two columns:
  - 'ciphertext': the encrypted text
  - 'cipher': the label indicating which cipher was used

Usage:
  For training:
    python cipher_model.py train --dataset ciphertexts.csv --epochs 10 --batch-size 16
  For prediction:
    python cipher_model.py predict "ciphertext"
  If no ciphertext is provided in predict mode, the script will prompt for input.

When training, the script saves:
  - The trained Keras model (default: 'cipher_classifier_model.h5')
  - The tokenizer (default: 'tokenizer.pkl')
  - The label encoder (default: 'label_encoder.pkl')
  - The maximum sequence length (default: 'max_seq.pkl')

Requirements:
  - TensorFlow (and Keras)
  - scikit-learn
  - pandas
  - numpy
  - pickle 
"""

import os
import sys
import argparse
import pickle
import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense, Dropout

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def load_data(filename):
    """
    Load dataset from a CSV file.

    The CSV should have the columns:
      - 'ciphertext': The encrypted text.
      - 'cipher': The label indicating which cipher was used.
    """
    df = pd.read_csv(filename)
    texts = df['ciphertext'].astype(str).tolist()
    labels = df['cipher'].tolist()
    return texts, labels

def prepare_data(texts, labels, test_size=0.2):
    """
    Preprocess texts and labels:
      - Encode labels into integers.
      - Tokenize ciphertexts at the character level.
      - Pad sequences to a uniform length.
      - Split the data into training and testing sets.
    """
    # Encode labels
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(labels)
    num_classes = len(label_encoder.classes_)
    print("Cipher classes:", label_encoder.classes_)

    # Tokenize at character level
    tokenizer = Tokenizer(char_level=True)
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)

    # Determine the maximum sequence length (ensure ciphertexts are long enough, e.g., 30+ characters)
    max_sequence_length = max(len(seq) for seq in sequences)
    print("Maximum sequence length:", max_sequence_length)

    # Pad sequences so that they all have the same length
    X = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')
    vocab_size = len(tokenizer.word_index) + 1  # +1 for the reserved index 0

    # Split into training and testing sets (stratified to maintain class balance)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y)
    return X_train, X_test, y_train, y_test, tokenizer, label_encoder, max_sequence_length, vocab_size, num_classes

def build_model(vocab_size, max_sequence_length, num_classes, embedding_dim=128):
    # Build a CNN

    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_sequence_length),
        Conv1D(filters=128, kernel_size=5, activation='relu'),
        GlobalMaxPooling1D(),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def create_tf_dataset(X, y, batch_size=16, shuffle=True):

    dataset = tf.data.Dataset.from_tensor_slices((X, y))
    if shuffle:
        dataset = dataset.shuffle(buffer_size=len(X))
    dataset = dataset.batch(batch_size).prefetch(tf.data.AUTOTUNE)
    return dataset

def train_model(args):
    # Train and save the model

    if not os.path.exists(args.dataset):
        print(f"Dataset file {args.dataset} does not exist.")
        sys.exit(1)
    texts, labels = load_data(args.dataset)
    X_train, X_test, y_train, y_test, tokenizer, label_encoder, max_sequence_length, vocab_size, num_classes = prepare_data(texts, labels)
    print("Training data shape:", X_train.shape)
    print("Test data shape:", X_test.shape)
    
    model = build_model(vocab_size, max_sequence_length, num_classes)
    model.summary()

    train_dataset = create_tf_dataset(X_train, y_train, batch_size=args.batch_size, shuffle=True)
    test_dataset = create_tf_dataset(X_test, y_test, batch_size=args.batch_size, shuffle=False)
    
    model.fit(train_dataset, epochs=args.epochs, validation_data=test_dataset)
    
    loss, accuracy = model.evaluate(test_dataset)
    print("Test accuracy: {:.2f}%".format(accuracy * 100))
    
    # Save the trained model and preprocessing objects.
    model.save(args.model_path)
    with open(args.tokenizer_path, 'wb') as f:
        pickle.dump(tokenizer, f)
    with open(args.label_encoder_path, 'wb') as f:
        pickle.dump(label_encoder, f)
    with open(args.max_seq_path, 'wb') as f:
        pickle.dump(max_sequence_length, f)
    
    print(f"\nModel saved as '{args.model_path}'")
    print(f"Tokenizer saved as '{args.tokenizer_path}'")
    print(f"Label encoder saved as '{args.label_encoder_path}'")
    print(f"Max sequence length saved as '{args.max_seq_path}'")

def predict_cipher(args):
    # Load model and predict
    
    for path in [args.model_path, args.tokenizer_path, args.label_encoder_path, args.max_seq_path]:
        if not os.path.exists(path):
            print(f"Required file {path} does not exist. Please ensure you have trained the model first.")
            sys.exit(1)
            
    model = tf.keras.models.load_model(args.model_path)
    with open(args.tokenizer_path, 'rb') as f:
        tokenizer = pickle.load(f)
    with open(args.label_encoder_path, 'rb') as f:
        label_encoder = pickle.load(f)
    with open(args.max_seq_path, 'rb') as f:
        max_sequence_length = pickle.load(f)
    
    if args.ciphertext:
        ciphertext = args.ciphertext
    else:
        ciphertext = input("Enter the ciphertext to classify: ")
    
    sequence = tokenizer.texts_to_sequences([ciphertext])
    padded_sequence = pad_sequences(sequence, maxlen=max_sequence_length, padding='post')
    prediction = model.predict(padded_sequence)
    predicted_index = np.argmax(prediction, axis=1)[0]
    predicted_cipher = label_encoder.inverse_transform([predicted_index])[0]
    
    print("\nPredicted cipher type:", predicted_cipher)

def main():
    parser = argparse.ArgumentParser(description="Ciphertext Classification: Train or Predict")
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    train_parser = subparsers.add_parser('train', help="Train the cipher classifier model")
    train_parser.add_argument('--dataset', type=str, required=True, help="Path to the CSV dataset file")
    train_parser.add_argument('--epochs', type=int, default=10, help="Number of training epochs")
    train_parser.add_argument('--batch-size', type=int, default=16, help="Batch size for training")
    train_parser.add_argument('--model-path', type=str, default='cipher_classifier_model.h5', help="Path to save the trained model")
    train_parser.add_argument('--tokenizer-path', type=str, default='tokenizer.pkl', help="Path to save the tokenizer")
    train_parser.add_argument('--label-encoder-path', type=str, default='label_encoder.pkl', help="Path to save the label encoder")
    train_parser.add_argument('--max-seq-path', type=str, default='max_seq.pkl', help="Path to save the max sequence length")
    
    predict_parser = subparsers.add_parser('predict', help="Predict cipher type of a given ciphertext")
    predict_parser.add_argument('ciphertext', type=str, nargs='?', default=None, help="The ciphertext to classify")
    predict_parser.add_argument('--model-path', type=str, default='cipher_classifier_model.h5', help="Path to the trained model")
    predict_parser.add_argument('--tokenizer-path', type=str, default='tokenizer.pkl', help="Path to the saved tokenizer")
    predict_parser.add_argument('--label-encoder-path', type=str, default='label_encoder.pkl', help="Path to the saved label encoder")
    predict_parser.add_argument('--max-seq-path', type=str, default='max_seq.pkl', help="Path to the saved max sequence length")
    
    args = parser.parse_args()
    
    if args.command == 'train':
        train_model(args)
    elif args.command == 'predict':
        predict_cipher(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
