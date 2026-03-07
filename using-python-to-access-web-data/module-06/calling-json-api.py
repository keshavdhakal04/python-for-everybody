import urllib.request
import urllib.parse
import json

base_url = "http://py4e-data.dr-chuck.net/opengeo?"

address = 'Dartmouth'

params = {'q': address}
url = base_url + urllib.parse.urlencode(params)

print("Retrieving", url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()

print("Retrieved", len(data), "characters")

info = json.loads(data)

plus_code = info["features"][0]["properties"]["plus_code"]

print("Plus code", plus_code)