import requests
import json
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import re
import html5lib
url = "https://siseveeb.voco.ee/veebivormid/sookla_menuu"


resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html5lib')
kood = str(soup)
kood = kood[7279:]
menuu = kood
for i in range(4):
    repl = ['<h3><strong>', '</strong></h3>', '<li class="list-group-item"><h2>', '<span class="label label-info pull-right">']
    menuu1 = menuu.replace(repl[i], ",abcdefghij,")

menuu = menuu.split(",abcdefghij,")

menuud = []
for i in range(1, len(menuu)-1, 2):
    menuud.append(menuu[i])
hinnad_raw = soup.find_all("span", class_="label label-info pull-right")
hinnad = []

for hind in hinnad_raw:
    hind.replace('<span class="label label-info pull-right">', " ")
    hind.replace('</span>', " ")
    hinnad.append(hind)
com = []
kood_final = re.split("<small>|</small>", kood)
for i in range(1, len(kood_final), 2):
    com.append(kood_final[i])


with open("json mite enam kasitsi.py", "w") as json_fail:
    json_fail.write("[")
i = 0
with open("json mite enam kasitsi.py", "a") as json_fail:
    for item in menuud:
        if item == "PRAED" or item == "SUPID" or item == "MAGUSTOIDUD" or item == "JOOGID":
            json_fail.write("   {")
            json_fail.write('       "nimetus": ' + item + ",")
            json_fail.write('       "toidud": [')
        else:
            json_fail.write("            {")
            json_fail.write('                "nimetus": ' + item + ",")
            json_fail.write('                "hind":' + hinnad[i] + ",")
            json_fail.write('                "lisainfo":' + com[i] + ",")
            i += 1

print(hinnad)
print(com)
print(menuud)
print(menuu)
