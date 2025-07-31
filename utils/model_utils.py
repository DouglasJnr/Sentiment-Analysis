from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import accuracy_score, f1_score

def create_rnn_model(vocab_size, embedding_dim=128, rnn_units=64, maxlen=100, num_classes=4):
    model = Sequential([
        Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=maxlen),
        SimpleRNN(rnn_units, return_sequences=False),
        Dropout(0.5),
        Dense(num_classes, activation='sigmoid')
    ])
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def evaluate_model(y_true, y_pred):
    y_pred_bin = (y_pred > 0.5).astype(int)
    acc = accuracy_score(y_true, y_pred_bin)
    f1 = f1_score(y_true, y_pred_bin)
    return acc, f1