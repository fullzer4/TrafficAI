import requests

url = "http://localhost:5000/predict"
image = open("../Model/data/images/road54.png", "rb")
response = requests.post(url, files={"image": image})
print(response.json())