import urllib
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

theurl = "https://www.nike.com/gb/men"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")

#req = Request('https://www.nike.com/gb/men', headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()
#soup = BeautifulSoup(webpage, "html.parser")

links = []
shoes = []

for i in soup.find_all("a"):
    links.append(i.get('href'))

for j in links:
    if 'shoes' in j:
        shoes.append(j)

f = open("shoeslinks.txt", "a")
for k in shoes:
    f.write(k + '\n')

f.close()