import urllib.request
import xml.etree.ElementTree as ET

Solundir_XML = ET.parse(urllib.request.urlopen('https://services.marinetraffic.com/api/exportvessel/v:5/17fdbadf0e1c4b98a8d6940e6fd0d0aa53b0dc7d/mmsi:258632000'))

root_Solundir = Solundir_XML.getroot()


def getLat():

    for CO in root_Solundir.iter('row'):
        LAT = (CO.get('LAT'))
        print('LAT: ' + str(LAT))
        return LAT

def getLon():
    for CO in root_Solundir.iter('row'):
        LON = (CO.get('LON'))
        print('LON: ' + str(LON))
        return LON

for TIME in root_Solundir.iter('row'):
    TIMESTAMP = (TIME.get('TIMESTAMP'))



 print('Dato og tid: ' + str(TIMESTAMP)
