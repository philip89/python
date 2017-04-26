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

fh = open('placeIdForThirdPage.txt', 'r')
for line in fh:
    placeID = line
    
#place = sys.argv[1]
#place = 'ChIJxaDD9bswXUgRNqIm8wIn8U4'
r = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid=' + str(placeID) + '&key=AIzaSyDAAgXnsBXOji1zlKaj0yjarUlVeUkJgsc')
data = r.json()





output_file = "brokenLine.html"
x_values = []
y_values = []

##########################################################################################################
dbconn6 = mysql.connector.connect(user = 'root', password = 'carlowithdip', host = 'localhost', database = 'project')

mycursor6 = dbconn6.cursor(buffered= True)

gymName2 = data['result']['name']

query6 = ("SELECT  name_table.gym_name, gym_rating.gym_rating, gym_rating.time from name_table inner join gym_rating on name_table.gym_id = gym_rating.gym_id;")


mycursor6.execute(query6)

for ( gym_name, gym_rating, time) in mycursor6:
        #print(gym_id)
    gym_Name = str(gym_name)
       # print(gym_name)
    if gym_Name == gymName2:
        gymRating = str(gym_rating)
        x_values.append(gymRating)
       
        timeInMonths = str(time)
        y_values.append(timeInMonths)
        #print(time)
        #gymID = str(gym_id)
########################
        
# The problem i was trying to solve here: When the user clicks on a gym on the reviews page The gym is automaticly added to the database
# I could not find a way to stop the gym being added again when the same gym was clicked so instead I just use a loop to save the first 5 results of the
# database search so that the graph is only made out of the 5 results

########################
#print(x_values)
#y_values= [int(x) for x in y_values]
#y_values.sort()
#print(y_values)
x_axis = [0]
y_axis = [0]
print(len(x_values))
if len(x_values) > 5:
    for i in range(5):
        x_axis.append(x_values[i])
        y_axis.append(y_values[i])
else:
    x_axis = x_values
    y_axis = y_values
y_axis = [int(x) for x in y_axis]
y_axis.sort()
print(x_axis)
print(y_axis)
#############################################################################################################
p = figure(plot_width = 330, plot_height = 200, x_axis_label = 'months', y_axis_label= 'review', title = gymName2, toolbar_location= None)







p.line(y_axis, x_axis, line_width = 2, color = '#FB6F7E')
html = file_html(p, CDN, "firstDatebaseTest.html")
fi = open('GraphTesting.html', 'w')
fi.write(html)
fi.close()
#save(p, filename = 'brokenLine.html')
#webbrowser.open_new('http://127.0.0.1/example/webPageThree.html')
##############################################################################################################
#dbconn2.commit()

mycursor6.close()
dbconn6.close()
