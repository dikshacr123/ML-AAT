import sys
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Step 1: Read and preprocess the training data
training_data = []
training_labels = []

# Ensure that the 'trainingdata.txt' file is in the same directory as this script
with open('trainingdata.txt', 'r') as file:
    num_lines = int(file.readline().strip())
    for _ in range(num_lines):
        line = file.readline().strip()
        category, document = line.split(' ', 1)
        training_data.append(document)
        training_labels.append(category)

# Convert labels to integers
training_labels = np.array(training_labels, dtype=int)

# Step 2: Extract features from the text documents
# Using TfidfVectorizer to convert text into numerical features
vectorizer = TfidfVectorizer()

# Step 3: Train a classifier
# Using Naive Bayes classifier
classifier = MultinomialNB()
model = make_pipeline(vectorizer, classifier)

# Train the model
model.fit(training_data, training_labels)

# Step 4: Read input documents from standard input
input_documents = []
input_lines = int(sys.stdin.readline().strip())
for _ in range(input_lines):
    document = sys.stdin.readline().strip()
    input_documents.append(document)

# Classify the new documents
predicted_categories = model.predict(input_documents)

# Output the predicted categories
for category in predicted_categories:
    print(category)
