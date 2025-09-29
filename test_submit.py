import requests

# URL of your Django submit API
url = "http://127.0.0.1:8000/submit/"

# Example submission data
data = {
    "task_id": 1,             # 1: Letter to a Character
    "user": "Alice",          # Replace with any username
    "submission": "My test letter"  # Text or image URL
}

# Send POST request
response = requests.post(url, json=data)

# Print response from backend
print("Status code:", response.status_code)
print("Response JSON:", response.json())
