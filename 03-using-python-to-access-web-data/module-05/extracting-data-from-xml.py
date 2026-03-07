import urllib.request
import xml.etree.ElementTree as ET

url = "http://py4e-data.dr-chuck.net/comments_2363264.xml"
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()

for result in counts:
    nums.append(int(result.text))  # convert to int and add to list
    print(result.text)             # optional debug

print('Count:', len(nums))
print('Sum:', sum(nums))