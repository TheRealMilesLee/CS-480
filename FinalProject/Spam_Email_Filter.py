# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
import os
import glob
data_path = 'trec05p-1'
emails = []

for root, dirs, files in os.walk(data_path):
    for file in glob.glob(os.path.join(root, '*.txt')):
        with open(file, 'r', encoding='ISO-8859-1') as f:
            text = f.read()
            emails.append(text)

print(emails)
print('Number of emails:', len(emails))

# tokenizer = keras.preprocessing.text.Tokenizer(num_words=10000)
# tokenizer.fit_on_texts(train_data['text'])

# train_sequences = tokenizer.texts_to_sequences(train_data['text'])
# test_sequences = tokenizer.texts_to_sequences(test_data['text'])
# train_data = keras.preprocessing.sequence.pad_sequences(
#     train_sequences, maxlen=100)
# test_data = keras.preprocessing.sequence.pad_sequences(
#     test_sequences, maxlen=100)

# model = keras.Sequential([
#     layers.Embedding(10000, 16, input_length=100),
#     layers.GlobalAveragePooling1D(),
#     layers.Dense(16, activation='relu'),
#     layers.Dense(1, activation='sigmoid')])

# model.compile(optimizer='adam', loss='binary_crossentropy',
#               metrics=['accuracy'])
# model.fit(train_data, train_labels, epochs=10,
#           batch_size=32, validation_split=0.2)
# results = model.evaluate(test_data, test_labels)
# print('Test accuracy:', results[1])
