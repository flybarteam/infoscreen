#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

url = 'https://www.marinetraffic.com/en/ais/details/ships/shipid:312357/mmsi:258632000/vessel:SOLUNDIR'
soup = BeautifulSoup(requests.get(url).text,"html.parser")

for i in soup.find_all('tr', attrs={'class':'table-row'}):
    print('[Data id] => {}'.format(i.get('data-id'))