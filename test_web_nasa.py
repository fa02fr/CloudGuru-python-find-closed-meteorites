# -*- coding: utf-8 -*-
# F. Arné 
# Doc
# https://docs.google.com/document/d/1yNpHXB5Ynx9Pir9U4QRu5IcqrvFdil_AGPiOk59mNmU/edit#heading=h.l4ntv5yhuxgo
# https://acloud.guru/course/python-for-beginners/learn/e41f93aa-5abc-e79c-df13-c04306b762fa/77b986cd-e55f-a3eb-9518-347d0cec9031/watch?backUrl=~2Fcourses
# Sources URL
# https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh

# Libraries
import requests
import math

# Constantes
v_dir = "s:\Data04 - Informatique\Applications\Python\CloudGuru_Meteorites\\"
v_debug = False

# https://www.latlong.net/ : Sartrouville
my_loc = (48.945820, 2.172220)

# Functions
## Distance entre 2 points de la terre
def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

## Return Distance is exists in element, if not infinite    
def get_dist(meteor):
    return meteor.get('distance', math.inf)

## >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
if __name__ == '__main__':
 
    meteor_resp = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
    meteor_data = meteor_resp.json()

    for meteor in meteor_data:
        if not ('reclat' in meteor and 'reclong' in meteor): continue
        meteor['distance'] = calc_dist(float(meteor['reclat']),
                                       float(meteor['reclong']),
                                       my_loc[0],
                                       my_loc[1])

    meteor_data.sort(key=get_dist)

    # print(meteor_data[0:10])
    for meteor in meteor_data[0:10]: 
        print(meteor['name'] + " à " + str(meteor['distance']) + " km")
        
        