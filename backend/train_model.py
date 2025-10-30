import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Example dummy dataset (Year, Temp, Rainfall)
data = {
    'year': [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024],
    'temperature': [28.5, 28.7, 29.0, 29.3, 29.7, 30.1, 30.3, 30.6],
    'rainfall': [1200, 1180, 1150, 1170, 1120, 1100, 1080, 1070]
}
df = pd.DataFrame(data)

# Train model
X = df[['year']]
y = df[['temperature', 'rainfall']]

model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'climate_model.pkl')

print("✅ Model trained and saved successfully!")

