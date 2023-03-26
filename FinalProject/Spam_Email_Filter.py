from sklearn.model_selection import train_test_split
import pandas as pd

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
messages = data['v2'].values
labels = data['v1'].values

# Split the data into training and validation sets
train_messages, train_labels = train_test_split(messages, labels)

print(train_labels)
