import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers
import pathlib
dataset_url = "https://plg.uwaterloo.ca/cgi-bin/cgiwrap/gvcormac/trec05p-1.tgz"
data_dir = tf.keras.utils.get_file(origin=dataset_url,
                                   fname='SpamEmails',
                                   untar=True)
data_dir = pathlib.Path(data_dir)


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
