<html>
<head>
<title> Gym Finder </title>
<link rel="stylesheet" type="text/css" href="stylesheet.css" media="screen" title="no title" charset="utf-8">
<style type = "text/css">

body{
	background-image: url("bg3.jpg");
   // background-size: 100% 100%;
   font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
#bar {
    height: 6%;
    width: 20%;
    margin-left:70%;
    margin-top: 5%;
    border: none;
	border-radius:5px;
}
#s {
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

#aim{
	position: absolute;
	color: white;
	width: 60%;
	font-size: 120%;
	padding-left:10px;
	padding-top:50px;
	text-align:justify;
	line-height:1.5;
	
}  
#borderDiv{
	position: absolute;
	height:450px;
	width:2px;
	background-color:#FB6F7E;
	margin-left:63%;
	margin-top:70px;
	
}
#contact{
	position: absolute;
	height:400px;
	width:350px;
	//background-color:white;
	//border:1px solid #FB6F7E;
	margin-left:70%;
	margin-top:87px;
	font-size: 110%;
	color: white;
	
	
}
#scrpits{
	color:white;
	position:absolute;
	margin-top: 24%;
	padding-left:10px;
	
}
#scrpits a{							
	text-decoration:none;
	color: #FFD2D2;
	position:relative;
	margin-top: 20px;
}
 #scrpits a:hover {
    color:#FB6F7E;
}
table, tr, td{
	padding:5px;
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
		<div id = "aim"> <p> About this website: <br><br> This webpage was built for a college project. The aim of the project was to use Python to extract information from open data APIs.		
		The information had to be saved to a MySQL database so that graphs could be created to see if the APIs information changed over time. A Webite  was designed
to display the API information, Maps and Graphs. The maps were created using a Python library called folium, the graphs using a library called bokeh.
The website employs the use of HTML5, CSS, JavaScript, PHP, Python and MySQL. The Scripts for the website can be viewd below	</p> </div>


<div id="scrpits">
	<table style="width:100%">
  <tr>
    <th>Python</th>
    <th>PHP</th> 
    <th>HTML</th>
  </tr>
  <tr>
    <td><a href="reviewsPage.py" target="_blank">thirdPageCreator.py</a></td>
    <td><a href="fPageSearch.txt" target="_blank">firstPageSearch.php</a></td> 
    <td><a href="mymap2.html" target="_blank">mapCreatedForSecondPage.html</a></td>
  </tr>
  <tr>
    <td><a href="searchFoliumCreator.py" target="_blank">firstMapCreator.py</a></td>
    <td><a href="sPageSearch.txt" target="_blank">secondPageSearch.php</a></td> 
    <td><a href="GraphTesting.html" target="_blank">graphCreatedForthirdPage.html</a></td>
  </tr>
   <tr>
    <td><a href="currentLocationFoliumMaker.py" target="_blank">secondMapCreator.py</a></td>
    <td><a href="lThirdPage.txt" target="_blank">thirdPageGymNames.php</a></td> 
   
  </tr>
   <tr>
    <td><a href="graphMakingProgram.py" target="_blank">graphCreator.py</a></td>
    <td><a href="cThirdPage.txt" target="_blank">thirdPageCountyBar.php</a></td> 
  
  </tr>
   <tr>
    <td><a href="firstDatebaseTest.py" target="_blank">savngInfoToDatabase.py</a></td>

  </tr>
</table>
		
		
	</div>
		<div id="borderDiv"> </div>
        <div id = "contact"> About Me:<br> <br>Name:  Philip Murphy <br><br>
		I am a Computer Science graduate looking for a career as a Software developer. <br> <br>
		
		Get in touch with me on Linkedin:<br><br>
		<a href="https://ie.linkedin.com/pub/philip-murphy/52/53a/33a" target="_blank">
			<img src="https://static.licdn.com/scds/common/u/img/webpromo/btn_myprofile_160x33.png" width="160" height="33" border="none" alt="View Philip Murphy's profile on LinkedIn">
		</a>
   </div>
	
</body>
</html>