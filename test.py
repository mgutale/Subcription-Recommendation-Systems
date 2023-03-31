import requests
import json

response = requests.post('http://localhost:5000/recommend', json={'user_id': 123})
recommendations = response.json()
with open('recommendations.json', 'w') as f:
    json.dump(recommendations, f)

print(recommendations)
