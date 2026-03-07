import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/known_by_Sukhvir.html'
count = int(input('Enter Count : '))
position = int(input('Enter Position : '))
print('Retrieving : ',url)
while count > 0 :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    nextLink = tags[position - 1]
    url = nextLink.get('href', None)
    count -= 1
    print('Retrieving : ',url)

     
    