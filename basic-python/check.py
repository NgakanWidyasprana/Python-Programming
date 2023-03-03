import requests

value = requests.get("http://www.google.com")

print(len(value.text))