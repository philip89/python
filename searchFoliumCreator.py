#! /usr/bin/env python
import requests
import json
import folium
import sys
import os

# This is taking an input from the PHP script
place = sys.argv[1]

# Being used to open a text file with the input from the php in it for testing
#fh = open('try.txt', 'w')
#fh.write(place)


r= requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=gym+in+' + str(place) + '+ireland&key=AIzaSyDQx-5VXedK2BZX1G0bcRxMmyZucKjKxhs')
d = r.json()


r2= requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + str(place) + ',+ireland&key=AIzaSyDQx-5VXedK2BZX1G0bcRxMmyZucKjKxhs')
d2 = r2.json()

lat = d2['results'][0]['geometry']['location']['lat']
long = d2['results'][0]['geometry']['location']['lng']

mymap2 = folium.Map(location=[lat, long], zoom_start=12)

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


mymap2.save('mymap2.html')

