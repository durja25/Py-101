import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_flags = ssl.CERT_NONE

url = input("url: ")
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

# Retrive all anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))