import requests
import json
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import html5lib
url = "https://siseveeb.voco.ee/veebivormid/sookla_menuu"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html5lib')
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if str(data).strip() != "":
            print("Encountered some data  :", data)
        else:
            pass
naidis = {
                "nimetus": "nim",
                "hind": "3.23",
                "lisainfo": "Väga hea"
            }

parser = MyHTMLParser()
parser.feed(str(soup))
with open("json kasitsi.py", "r") as file:
    data = json.load(file)
data.append(entry)