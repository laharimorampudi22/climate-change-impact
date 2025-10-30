import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv('data.csv')

# Train simple regression model
X = df[['year']]
y = df[['temperature', 'rainfall']]

model = LinearRegression()
model.fit(X, y)

# Save trained model
joblib.dump(model, 'climate_model.pkl')
print("✅ Model trained successfully using data.csv!")
