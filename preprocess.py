import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv('data.csv')

# Remove missing values
data = data.dropna()

# Remove duplicates
data = data.drop_duplicates()

# Normalize numerical features
scaler = StandardScaler()
data[['feature1', 'feature2']] = scaler.fit_transform(data[['feature1', 'feature2']])

print("Preprocessing completed!")