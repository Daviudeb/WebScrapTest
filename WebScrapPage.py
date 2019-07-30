import urllib
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

userInputWeb = input("Please enter a website link: ")

webpage = None
fileName = ""

try:
    webpage = urllib.request.urlopen(userInputWeb)
except:
    req = Request(userInputWeb, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

links = []
shoes = []

for i in soup.find_all("a"):
    links.append(i.get('href'))
for j in links:
    if isinstance(j,str):
        if 'shoes' in j:
            shoes.append(j)

fileName = soup.title.text
f = open("shoes" + str(len(fileName)) + ".txt", "a")
for k in shoes:
    if isinstance(k, str):
        f.write(k + '\n')
f.close()