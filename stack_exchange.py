import json
import sys
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer

# Ensure raw_input is properly assigned for Python 3
if sys.version_info[0] >= 3:
    raw_input = input

transformer = HashingVectorizer(stop_words='english')

# Load training data
_train = []
train_label = []
try:
    with open('training.json') as f:
        for i in range(int(f.readline().strip())):
            h = json.loads(f.readline().strip())
            _train.append(h['question'] + "\r\n" + h['excerpt'])
            train_label.append(h['topic'])
except (IOError, ValueError) as e:
    print(f"Error reading training data: {e}")
    sys.exit(1)
