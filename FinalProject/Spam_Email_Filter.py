import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix)
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

FilePath = 'spam.csv'
processedFilePath = 'Processed.csv'
with open(FilePath, 'rb') as csv_in:
    with open(processedFilePath, "w", encoding="utf-8") as csv_temp:
        for line in csv_in:
            if not line:
                break
            else:
                line = line.decode("utf-8", "ignore")
                csv_temp.write(str(line).rstrip() + '\n')
# Load the CSV file into a pandas dataframe
data = pd.read_csv(processedFilePath, encoding='utf-8')

# Extract the message and label columns
labels = data['v1'].values
messages = data['v2'].values

train_Msg, validate_Msg, train_label, validate_label = train_test_split(
    messages, labels)

# Create a count vectorizer to convert text to a matrix of token counts
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(train_Msg)
X_test_counts = vectorizer.transform(validate_Msg)
# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_counts, train_label)

# Make predictions on the test set
y_pred = clf.predict(X_test_counts)

# Evaluate the classifier's performance
print("Accuracy:", accuracy_score(validate_label, y_pred))
print("Confusion Matrix:\n", confusion_matrix(validate_label, y_pred))
print("Classification Report:\n", classification_report(validate_label, y_pred))
