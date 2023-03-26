from sklearn.model_selection import train_test_split
import pandas as pd


# Load the CSV file into a pandas dataframe
data = pd.read_csv('spam.csv', encoding='utf-8')

# Extract the message and label columns
messages = data['v2'].values
labels = data['v1'].values

# Split the data into training and validation sets
train_messages, train_labels = train_test_split(messages, labels)

print(train_labels)
