import requests
import json
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import re
import html5lib
url = "https://siseveeb.voco.ee/veebivormid/sookla_menuu"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html5lib')
menuud = soup.find_all("div", class_="panel-heading text-center")
soogid = soup.find_all("li", class_="list-group-item")
hinnad = []
hinnad = soup.find_all("span", class_="label label-info pull-right")
com = []
kood = str(soup)
kood = kood[7279:]
kood_final = re.split("<small>|</small>", kood)
for i in range(1, len(kood_final), 2):
    com.append(kood_final[i])
naidis = {
                "nimetus": "nim",
                "hind": "3.23",
                "lisainfo": "Väga hea"
            }



with open("json kasitsi.py", "r") as file:
    data = json.load(file)
#data.append(entry)
print(menuud)
print(soogid)
print(hinnad)
print(com)
