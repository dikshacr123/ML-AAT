import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

# Load in training data

fname = 'trainingdata.txt'

targets = []
data = []

with open(fname) as f:
    for line in f:
        targets.append(line[0])
        data.append(line[2:].strip())

# Train the classifier

textClf = Pipeline([('vect', CountVectorizer(max_df=0.85)),
                    ('tfidf', TfidfTransformer()),
                    ('clf', SGDClassifier()),])
textClf.fit(data, targets)

# Load in test data


input = sys.stdin.read
input_data = input().split('\n')

n = int(input_data[0].strip())
docs = input_data[1:n+1]

# Predict

predicted = textClf.predict(docs)

# Output in hackerrank format

for pred in predicted:
    print(pred)
