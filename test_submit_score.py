import requests

url = "http://127.0.0.1:5000/submit_score"
data = {
    "name": "Player1",
    "score": 1000
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.text)  # Print the raw response text