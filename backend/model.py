import joblib
import numpy as np
import pandas as pd

# Load model trained earlier
model = joblib.load('climate_model.pkl')

def predict_future(years):
    """Predict temperature and rainfall for next N years"""
    future_years = np.arange(2025, 2025 + years)
    X_future = pd.DataFrame({'year': future_years})
    preds = model.predict(X_future)
    return {
        "future_years": future_years.tolist(),
        "predicted_temp": [round(float(p[0]), 2) for p in preds],
        "predicted_rain": [round(float(p[1]), 2) for p in preds]
    }

