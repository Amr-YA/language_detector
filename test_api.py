import requests
def healthcheck():
    port = "3000"
    method = "healthcheck"
    host = f'http://localhost:{port}/{method}'
    r = requests.get(host)
    return r.text

def predict():
    port = "3000"
    method = "predict"
    host = f'http://localhost:{port}/{method}'
    text = "welcome"
    r = requests.post(host, json={"sender": "test_id", "message": text})
    return r.text

print(predict())
