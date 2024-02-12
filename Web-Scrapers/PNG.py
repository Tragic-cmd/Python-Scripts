# PNG Scraper

import requests
from bs4 import BeautifulSoup

site_map = 'https://pngimg.com/sitemap4.xml'

response = requests.get(site_map)

xml = response.text

soup = BeautifulSoup(xml,'xml')
soup.find_all('loc')

site_map_1 = site_maps[0]

response = requests.get(site_map_1)

soup = BeautifulSoup(response.text,'xml')
soup.find_all('href')

master_list = []
for loc in soup.find_all('loc'):
    url = loc.text
    master_list.append(url)

master_list[0:5]
soup
site_maps
