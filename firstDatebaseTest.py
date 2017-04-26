#! /usr/bin/env python
import mysql.connector
import requests
from bokeh.plotting import figure, output_file, show
import time
import webbrowser
#####
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
#####
fh = open('placeIdForThirdPage.txt', 'r')
for line in fh:
    placeID = line
    
#place = sys.argv[1]
#place = 'ChIJxaDD9bswXUgRNqIm8wIn8U4'
r = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid=' + str(placeID) + '&key=AIzaSyDAAgXnsBXOji1zlKaj0yjarUlVeUkJgsc')
data = r.json()





#############################################################################################################################
# This is entering the data into the name_table. Just the name as the id is auto increment
dbconn = mysql.connector.connect(user = 'root', password = 'carlowithdip', host = 'localhost', database = 'project')

mycursor = dbconn.cursor()
#print (data['result']['name'])
gymName = data['result']['name']


query = ("insert into name_table(gym_name) values('" + str(gymName) + "')")


mycursor.execute(query)

dbconn.commit()

mycursor.close()
dbconn.close()
#############################################################################################################################

#############################################################################################################################

#############################################################################################################################
# This is being used to open the database and take the gym_id from the name_table so that I can use it in the rating_table
dbconn2 = mysql.connector.connect(user = 'root', password = 'carlowithdip', host = 'localhost', database = 'project')

mycursor2 = dbconn2.cursor(buffered= True)



query2 = ("SELECT MAX(gym_id) FROM name_table")


mycursor2.execute(query2)

for (gym_id) in mycursor2:
        #print (gym_name)
        gymID = str(gym_id)



#dbconn2.commit()

mycursor2.close()
dbconn2.close()
#############################################################################################################################
# This is taking in the last gym_id and splitting it from (12,) to 12
part = gymID.split('(')
part1 = part[1].split(')')
part2 = part[1].split(',')
print(part2[0])

#############################################################################################################################
dbconn3 = mysql.connector.connect(user = 'root', password = 'carlowithdip', host = 'localhost', database = 'project')

mycursor3 = dbconn3.cursor()


for p in data['result']['reviews']:
    gymR = p['rating']
    gymRList = p['relative_time_description']
    gymRatingList = gymRList.split(' ')
    if(gymRatingList[0].isdigit()):
        time = gymRatingList[0]
    else:
        time = 1
    #time = '3'
    query3 = ("insert ignore into gym_rating(gym_rating, time, gym_id) values('" + str(gymR) + "','" + str(time) + "','" + str(part2[0]) + "')")
    mycursor3.execute(query3)

dbconn3.commit()

mycursor3.close()
dbconn3.close()


###############################################################################################################################
#########################################################################################################
