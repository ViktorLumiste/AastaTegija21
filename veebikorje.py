import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
url = "http://192.168.22.172/menu-example/"
resp = requests.get(url)