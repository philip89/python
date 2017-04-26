#! /usr/bin/env python
import requests
import json
import folium
import sys
import os
from glob import glob

name = sys.argv[1]
name = name.split('-')
#long = 7.2448
#lat = 52.6541
r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=' + str(name[0]) + ',' + '-'+ str(name[1]) + '&key=AIzaSyDQx-5VXedK2BZX1G0bcRxMmyZucKjKxhs')
data = r.json()

#' + str(name[0]) + ',' + '-'+ str(name[1]) + '
place = data['results'][0]['address_components'][4]['long_name']
#print(place)

r= requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=gym+in+' + str(place) + '&key=AIzaSyDQx-5VXedK2BZX1G0bcRxMmyZucKjKxhs')
d = r.json()
#53.1424, -7.6921
lat1 = str(name[0])
long1 = '-' + name[1]
mymap2 = folium.Map(location=[lat1, long1], zoom_start=13)
for i in range(len(d['results'])):
    name = d['results'][i]['name']
        #print(name)
    placeid = d['results'][i]['place_id']
       # print(placeid)
    lat = d['results'][i]['geometry']['location']['lat']
       # print(lat)
    long = d['results'][i]['geometry']['location']['lng']
       # print(long)
    #    print(' ')
    folium.Marker([lat, long], popup=name).add_to(mymap2)

folium.Marker([lat1, long1], popup='you are here', icon=folium.Icon(color ='red')).add_to(mymap2)

mymap2.save('mymap2.html')
