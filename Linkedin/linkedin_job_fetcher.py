import requests

def fetchAndSave(url, path):
    r = requests.get(url)
    # Use UTF-8 encoding to handle special characters
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

