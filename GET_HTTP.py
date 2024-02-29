import requests

r = requests.get("https://api.github.com/search/repositories",
    params={"q": "python"}             
)
print(r.status_code)
print(r.json())

data = r.json()
print(data.keys())