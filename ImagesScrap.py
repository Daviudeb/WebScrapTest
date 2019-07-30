import urllib
import os
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

print("Web Scraping Images")

while True:
    userInputWeb = input("Please enter a website link: ")

    if userInputWeb:
        webpage = None
        fileName = ""

        try:
            webpage = urllib.request.urlopen(userInputWeb)
        except:
            req = Request(userInputWeb, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()

        soup = BeautifulSoup(webpage, "html.parser")

        dirName = soup.title.text

        try:
            os.mkdir(dirName)
            print("Directory ", dirName, " Created")
        except:
            print("Directory ", dirName, " already exists.")

        images = []

        for i in soup.find_all('img'):
            images.append(i.get('src'))

        print(images)

        imageLinks = []

        for j in images:
            if isinstance(j,str):
                imageLinks.append('https:' + j)
        print(imageLinks)

        imageName = ""
        for k in imageLinks:
            imageName = k.split('/')[-1]
            try:
                if ('jpg' in imageName) | ('png' in imageName):
                    fullFileName = os.path.join(dirName,imageName)
                    urllib.request.urlretrieve(k,fullFileName)
            except Exception as e:
                print(e)
                print("There was an issue with this link: %s" % k)
    else:
        break