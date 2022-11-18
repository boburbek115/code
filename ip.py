# https://atomi.tk/ip/
import json
import requests
from bs4 import BeautifulSoup


response = requests.get("https://atomi.tk/ip/")
soup = BeautifulSoup(response.text , 'lxml')
response_main = soup.find('pre')
response_text = response_main.text
print(response_text)
