import requests
import json
import os
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import re
import html5lib
url = "https://siseveeb.voco.ee/veebivormid/sookla_menuu"


resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html5lib')
kood = str(soup)
kood = kood[7350:]
menuu = kood
for i in range(4):
    repl = ['<h3><strong>', '</strong></h3>', '<li class="list-group-item"><h2>', '<span class="label label-info pull-right">']
    print(repl[i])
    menuu = menuu.replace(repl[i], ",abcdefghij,")
menuu = menuu.split(",abcdefghij,")
menuud = []
for i in range(1, len(menuu), 2):
    menuud.append(menuu[i])
hinnad_raw = soup.find_all("span", class_="label label-info pull-right")
hinnad = []

for hind in hinnad_raw:
    hind1 = str(hind)
    hind2 = hind1.replace('<span class="label label-info pull-right">', "")
    hind3 = hind2.replace('</span>', "")
    hinnad.append(hind3)
com = []
kood_final = re.split("<small>|</small>", kood)
for i in range(1, len(kood_final), 2):
    com.append(kood_final[i])


with open("json mite enam kasitsi.py", "w") as json_fail:
    json_fail.write("[")
i = 0
with open("json mite enam kasitsi.py", "a") as json_fail:
    for item in menuud:
        if item == "PRAED":
            json_fail.write("\n   {")
            json_fail.write('\n       "nimetus": "' + item + '",')
            json_fail.write('\n       "toidud": [')
        elif item == "SUPID" or item == "MAGUSTOIDUD" or item == "JOOGID":
            json_fail.write("\n       ]")
            json_fail.write("\n   },")
            json_fail.write("\n   {")
            json_fail.write('\n       "nimetus": "' + item + '",')
            json_fail.write('\n       "toidud": [')
        #elif (i<(len(menuud)-2)):
         #   if menuud[i+1] == "SUPID" or item[i+1] == "MAGUSTOIDUD" or item[i+1] == "JOOGID":
          #      json_fail.write("\n            {")
           #     json_fail.write('\n                "nimetus": "' + item + '",')
            #    json_fail.write('\n                "hind": "' + hinnad[i] + '",')
             #   json_fail.write('\n                "lisainfo": "' + com[i] + '",')
              #  json_fail.write("\n            }")
               # i += 1
            #else:
             #   json_fail.write("\n            {")
              #  json_fail.write('\n                "nimetus": "' + item + '",')
               # json_fail.write('\n                "hind": "' + hinnad[i] + '",')
                #json_fail.write('\n                "lisainfo": "' + com[i] + '",')
                #json_fail.write("\n            },")
                #i += 1

        else:
            json_fail.write("\n            {")
            json_fail.write('\n                "nimetus": "' + item + '",')
            json_fail.write('\n                "hind": "' + hinnad[i] + '",')
            json_fail.write('\n                "lisainfo": "' + com[i] + '",')
            json_fail.write("\n            },")
            i += 1
    json_fail.write("\n      ]")
    json_fail.write("\n   }")
    json_fail.write("\n]")

