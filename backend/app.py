from flask import Flask, request, jsonify
from model import predict_future

app = Flask(__name__)

@app.route('/')
def home():
    return "🌍 Climate Change Predictor API Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        years = int(data.get('years', 1))
        prediction = predict_future(years)
        return jsonify(prediction)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
