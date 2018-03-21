import sys
import re
import requests
import urllib.request
from bs4 import BeautifulSoup


#Checking for at least one command line argument
if len(sys.argv) == 1:
    print('Not enough arguments')
    sys.exit()

#Downloading the information from the URL
resp = urllib.request.urlopen(sys.argv[1])
#Creating the BeautifulSoup Object to parse the webpage
soup = BeautifulSoup(resp, "html.parser")
print("Given URL: " )
print(sys.argv[1])
#Looping through all the links
for link in soup.find_all('a', attrs={'href': re.compile("^http:")}):
    #This cleanly and elegantly deals with any redirects.
        r = requests.head(link['href'], allow_redirects=True)
        print(r.url)
        if r.headers["Content-Type"] == "application/pdf":
            print("URL: ")
            print(r.url)
            print("Length in bytes: ")
            print(r.headers["Content-Length"])
            print()
