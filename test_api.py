#%%
import requests

host = 'http://localhost:5005/predict'
text = "اهلا"

r = requests.post(host, json={'sender': 'amr', 'message': text})

print(r.text)
# %%
