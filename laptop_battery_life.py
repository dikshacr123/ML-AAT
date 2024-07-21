#!/bin/python3

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# Define the path to the training data file
file_path = 'trainingdata.txt'

# Read the dataset
dataset = pd.read_csv(file_path, header=None)

# Plot the data
plt.plot(dataset.iloc[:, 0], dataset.iloc[:, 1], 'ro')
plt.ylabel('Laptop Battery Life')
plt.xlabel('Charging Time')
plt.show()

# Remove items with battery life greater than 8 hours
dataset = dataset[dataset.iloc[:, 1] < 8]

# Prepare the data for linear regression
# Add bias (the code inserts at the wrong column, correct column index is 0)
dataset.insert(0, 'Bias', 1)

# Separate dependent and independent variables
X = dataset.iloc[:, 0:2].to_numpy()
Y = dataset.iloc[:, 2].to_numpy()

# Create the linear regression model
model = linear_model.LinearRegression()
model.fit(X, Y)

# Get user input for the charging time
timeCharged = float(input().strip())

# Predict the battery life
result = model.predict([[1, timeCharged]])  # Note: Bias is 1 for all inputs
if result[0] > 8:
    print(8.0)
else:
    print(round(result[0], 2))
