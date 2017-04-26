#! /usr/bin/env python
### This bac up was made when the search bar was on the page ie before i tried to put a list for picking places

import requests
import folium
import subprocess
import cgi
import sys
import io
#subprocess.call(['rm', 'web1.html'])

county = sys.argv[1]

filehandlerThird = open('placeIdforThirdPage.txt', 'r')
for line in filehandlerThird:
    placeId = line

############################################################################
fh = io.open('thirdPage.html', 'w', encoding='utf8')
r = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid='+ str(placeId) +'&key=AIzaSyDQx-5VXedK2BZX1G0bcRxMmyZucKjKxhs')
data = r.json()
############################################################################
#countyhandler = open('county.txt', 'r')
#for countyline in countyhandler:
#    county = countyline
#county = sys.argv[1]
############################################################################
reqList= requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query=gym+in+' + str(county) + '+ireland&key=AIzaSyDQx-5VXedK2BZX1G0bcRxMmyZucKjKxhs')
dataList = reqList.json()
#print(data)
day = ''
time = ''



fh.write("""<html>
            <body>
            
            <meta name="viewport" content="width=device-width">
            <head>
            <title> Gym Finder </title>
            <style type = "text/css">
                body{
                   background-image: url("bg3.jpg");
                   //height:100%;
                }
                #bar {
                    height: 6%;
                    width: 20%;
                    margin-left:75%;
                    margin-top: 2%;
                    border: none;
                    border-radius:5px;
                    font-size:110%;
		font-family: Arial, Helvetica, sans-serif;
                }
                #s {
                    height: 5%;
                    width: 8%;
                    margin-left:75%;
                    margin-top: 1%;
                    border: none;
                    border-radius:5px;
                    background-color:#FB6F7E;
                    color: white;
                }
                #c {
                    height: 5%;
                    width: 12%;
                    margin-left:1%;
                    margin-top: 1%;
                    border: none;
                    border-radius:5px;
                    background-color:#FB6F7E;
                    color: white;
                }
               
                #n {
                    width: 90%;
                    //height: 20%;
                    padding: 2%;
                    margin-left: 10%;
                    font-family: Arial, Helvetica, sans-serif;
                    font-weight: 400;
                    font-size: 250%;
                    color: white;
                }
                #o{
                    margin-left: 10%;
                    color:white;
                    font-family: Arial, Helvetica, sans-serif;
                   
                }
                
                 #nameopenholder {
                    width: 25%;
                    border: 1px solid white;
                    margin-left:75%;
                    
                }
              
                #review{
                    position: absolute;
                    width: 50%;
                    top: 23%;
                    left: 22%;
                    line-height:1.5;
                    border-collapse: collapse;
                    color:white;
                    //border: 1px solid white;
                    font-family: Arial, Helvetica, sans-serif;
                }
                 #pid {
                     position: absolute;
                    width: 50%;
                    top: 28%;
                    left: 22%;
                    line-height:1.5;
                    border-collapse: collapse;
                    color:white;
                    border: 1px solid white;
                    font-family: Arial, Helvetica, sans-serif;
                }
                input[type=text]{
                    background-color: white;
                
                } 
                ul{
                    position: absolute;
                    width:200px;
                    border:none;
                    top: 20%;
                }
                #list li{
                    list-style-type: none;
                
                }
                input[type=submit]{
                     outline:none;
                    width:250px;
                    padding: 12px 20px;
                    margin-top: -18;
                    margin-left: -35;
                    border: none;
                   background-color:  #274C67;
                   // background:  linear-gradient(to bottom, #6db3f2 0%,#3690f0 31%,#54a3ee 50%,#1e69de 100%); 
                    color: white;
                 font-family: Arial, Helvetica, sans-serif;
               }
                   input[type=submit]:hover { 
                            background-color: #4887B3;
                    }

             #thirdDiv{
                position: relative;
                width:110%;
                height: 10%;
                background-color:#274C67;
                top:-2%;
                left: -2%;
                border-bottom: 1px solid white;
             }
            
            #thirdDiv p{
                position: relative;
		top:1em;
		padding-right:3%;
		float:left;
		font-family: Arial, Helvetica, sans-serif;
                //width:5%;
                left:20%;
                //color: white;
               
            }
           #thirdDiv a{							/* this is used to get rid of standard style on the links*/
		text-decoration:none;
		color: white;
            }

            #thirdDiv a:hover {
                color:#FB6F7E;;
            }
     
                    iframe {
               position: absolute;
	width:26%;
	height: 55%;
	margin-left:72.8%;
	margin-top: 2%;
	border: none;
}

        h2{
        color: white;
        font-family: Arial, Helvetica, sans-serif;
        padding-left: 10px;
        }

         h3{
        color: white;
        position: absolute;
        font-family: Arial, Helvetica, sans-serif;
        margin-top: -150px;
        padding-left: 74%;
        
        }
        
            </style>
            </head>
                <div id="thirdDiv">
                        <p><a href="firstPage.php">HOME</a></p>
                        <p><a href="secondPage.php"> MAP</a></p>
                        <p><a href="thirdPage.html"> REVIEWS</a> </p>
                        <p><a href="forthPage.php">ABOUT</a></p>
                       
		</div>
            <h2> Select a gym </h2>
            <form action="countyThirdPage.php" method="post" >
                            
			<input id = "bar" type="text" name="countyBar" placeholder="County...">
			<input id="s" type="submit" value="Submit">
	    </form>

	    <h3> Enter a county to see gyms in that county </h3>

            <div id="nameopenholder">
	    """)

# This is the name of the gym

name = data['result']['name']
fh.write("""<div id ="n">%s</div> """%(name))



# This for loop is going through the opening times and saving them in a table format
try:
    fh.write(""" <table id ="o"> <tr><th>Day</th><th>Times</th></tr>""" )
    oh =data['result']['opening_hours']['weekday_text']
    for line in oh:
        if line.startswith('M'):
            parts = line.split(': ')
            day = parts[0]
            time = parts[1]
        elif line.startswith('Tue'):
            parts = line.split(': ')
            day = parts[0]
            time = parts[1]
        elif line.startswith('Wed'):
            parts = line.split(': ')
            day = parts[0]
            time = parts[1]
        elif line.startswith('Thurs'):
            parts = line.split(': ')
            day = parts[0]
            time = parts[1]
        elif line.startswith('Fri'):
            parts = line.split(': ')
            day = parts[0]
            time = parts[1]
        elif line.startswith('Sat'):
            parts = line.split(': ')
            day = parts[0]
            time = parts[1]
        elif line.startswith('Sun'):
            parts = line.split(': ')
            day = parts[0]
            time = parts[1]
        opening = '<tr>' + '<td>' + day + '</td><td>' + time + '</td>' + '</tr>'
        fh.write(opening)
except KeyError:
        opening = '<tr>' + '<td> <br> Sorry no opening hours available <br> </td>' + '</tr>'
        fh.write(opening)
fh.write("""</table>""")
fh.write("""</div>""")

##############################################################################

count = 0
fh.write("""<ul id = "list">""")
for i in range(len(dataList['results'])):
    name = dataList['results'][i]['name']
    pId = dataList['results'][i]['place_id']
    listhtml = '<li>' + '<form action="listThirdPage.php" method="post">' +'<input name="placeidSearch" type="hidden" value ="'+ pId + '"/>'+ '<input class="nameID" name="listSearch" type="submit" value ="'+ name + '"/>' + '</form>'  + '</li>'    
    fh.write(listhtml)
fh.write("""</ul>""")

#############################################################################
# This for loop is going through the reviews and saving them to teh file
ratings = ''
fh.write(""" <table id ="review"> <tr><th >Rating</th><th style=" width:15%; padding-top:-20%;">Time Since</th><th>Reviews</th></tr>""" )
try:
    p = data['result']['reviews']
    for p in data['result']['reviews']:
        rating = p['rating']
        month = p['relative_time_description']
        texts = p['text']
        review = '<tr>' + '<td>' + str(rating) + '</td><td style="margin-top:-20%;">' + month + '</td><td>' + texts + '</td>' + '</tr>'
        fh.write(review)
       
except KeyError:
     fh.write("""<p id= "pid"> Sorry no reviews available for this at this time </p>""")
fh.write("""</table>""")
fh.write("""
            
            
             <!--<iframe src= "http://127.0.0.1/example/GraphTesting.html">-->
            </body>
            <script>
                
            
            </script>
            </html>""") 
fh.close()
