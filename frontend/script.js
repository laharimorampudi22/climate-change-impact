async function getPrediction() {
  const years = document.getElementById('years').value;
  const response = await fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({years: years})
  });
  const data = await response.json();
  document.getElementById('output').innerText = JSON.stringify(data, null, 2);
}

