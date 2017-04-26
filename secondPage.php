<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<title> Gym Finder </title>
<link rel="stylesheet" type="text/css" href="stylesheet.css" media="screen" title="no title" charset="utf-8">
<style type = "text/css">

body{
	background-image: url("bg3.jpg");
    //background-size: 100%;
}
#bar {										/* This is styling the search bar*/
    height: 6%;				
    width: 20%;
    margin-left:70%;
    margin-top: 5%;
    border: none;
	border-radius:5px;
	font-size:110%;
}
#s {										/* This is styling the search button*/
    height: 6%;
    width: 8%;
    margin-left:91%;
    margin-top: -2.8%;
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
    height: 20%;
    padding: 2%;
    margin-left: 10%;
    font-family: Arial, Helvetica, sans-serif;
    font-weight: 400;
    font-size: 250%;
    color: white;
}
table{
    margin-left: 10%;
    color:white;
    font-family: Arial, Helvetica, sans-serif;
}
#nameopenholder {
    width: 25%;
    height: 40%;
	border: 1px solid white;
	margin-left:70%;
}
iframe {
    position: absolute;
	width:58%;
	height: 69%;
	margin-left:5%;
	margin-top: -3%;
	border: none;
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
    color: white;
}
#thirdDiv a{							
	text-decoration:none;
	color: white;
}
 #thirdDiv a:hover {
    color:#FB6F7E;
}
h1{
    color:white;
}

#text{
	color:white;
	position: absolute;
	margin-left:69.2%;
	margin-top:3%;
	font-size: 110%;
	font-family: Arial, Helvetica, sans-serif;
	
} 
#text1{
	color:white;
	position: absolute;
	width: 400px;
	line-height:2;
	margin-left:69.2%;
	margin-top:3%;
	font-size: 110%;
	font-family: Arial, Helvetica, sans-serif;
	
} 
h1{
	width: 400px;
	padding-bottom: 10px;
	color:white;
	position: absolute;
	margin-top: -8%;
	margin-left: 5%;
	//font-size: 200%;
	font-family: Arial, Helvetica, sans-serif;
	border-bottom: 1px solid white;
}


</style>
</head>
<body>
	
	
	
	<div id="thirdDiv">
		<p><a href="firstPage.php">HOME</a></p>
		<p><a href="secondPage.php">MAP</a></p>
		<p><a href="thirdPage.html">REVIEWS</a> </p>
		<p><a href="forthPage.php">ABOUT</a></p>
    </div>

    <div id="text">  Search Gyms by County </div>
            
    <form action="secondPageSearch.php" method="post" >
        <input id = "bar" type="text" name="search" placeholder="County..">
		<input id="s" type="submit" value="Submit">
	</form>
	
	
	<h1> Gyms in <?php session_start(); echo $_SESSION['firstMessage']; ?> </h1>
	
	
	<div id="text1">  This page generates maps using a python library called 'folium'. The markers on the map shows
						all the gyms that google make available through their API, within a 5 kilometer radius of the area you have choosen.
						The gyms are marked with blue markers. Click on each marker to see the name of the gym.
						If you used the current location option on the first page then you will see a red marker aswel. 
						This indicates your current location.  </div>
		
		
    <iframe src= "mymap2.html">	
	
	
	
</body>
</html>