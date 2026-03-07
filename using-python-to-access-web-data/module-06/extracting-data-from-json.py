import urllib.request
import json

url = 'http://py4e-data.dr-chuck.net/comments_2363265.json'

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

print("Retrieved", len(data), "characters")

info = json.loads(data)

counts = info["comments"]

total = 0
for item in counts:
    total += item["count"]

print("Count:", len(counts))
print("Sum:", total)