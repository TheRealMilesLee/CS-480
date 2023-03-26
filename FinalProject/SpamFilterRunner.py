import pickle

with open('spam_classifier_model.pkl', 'rb') as f:
    loaded_clf = pickle.load(f)

with open('count_vectorizer.pkl', 'rb') as f:
    loaded_vectorizer = pickle.load(f)

sample_text = ["Free entry to win a prize!"]
sample_text_counts = loaded_vectorizer.transform(sample_text)
prediction = loaded_clf.predict(sample_text_counts)
print("Prediction:", prediction[0])
