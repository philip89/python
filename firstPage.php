<html>
 <head>
    <title> Gym Finder </title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<style type = "text/css">

	body{
		background-image: url("bg2.jpg");
		 background-size: 100% 100%;
	}
	
	
	#header{
		padding-left: 20%;
		
		font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		color:white;
	}
	#header h1{
		font-size:200%;
		font-family: Arial, Helvetica, sans-serif;
		padding-top:25%;
		padding-left:60%;
	}
	
	#bar {
		height: 5%;
		width: 20%;
		margin-left:60%;
		margin-top: 10%;
		border: none;
		border-radius:5px;
		font-size:110%;
		font-family: Arial, Helvetica, sans-serif;
		
	}
	
	#s {
		height: 5%;
		width: 10%;
		margin-left:81%;
		margin-top: -3%;
		border: none;
		border-radius:5px;
		background-color:#FB6F7E;
		color: white;
		
		font-family: Verdana, Geneva, sans-serif;

	}
	#c {
		height: 5%;
		width: 31%;
		margin-left:60%;
		margin-top: -1%;
		border: none;
		border-radius:5px;
		background-color:#FB6F7E;
		color: white;
		
		font-family: Verdana, Geneva, sans-serif;
	}
	#bottomtext p{
		margin-left:60%;
		margin-top: 0.3%;
		font-family: Verdana, Geneva, sans-serif;
		font-size:75%;
	}
	#working{
		font-family: Verdana, Geneva, sans-serif;
		color:white;
		position: absolute;
		margin:0 auto;
	}
</style>
  
 </head>
 <body>
		<div id="working">  This Page is currently under construction. Some features may not display on certain browsers or devices   </div>
	
		<div id="header">
			<h1> FIND GYMS NEAR YOU!</h1>
		
		
	<form action="firstPageSearch.php" method="post">
			<input id="bar" type="text" name="search" placeholder="Search..">
			<input id="s" type="submit" value="Submit"> 
	</form>
	
	<form action="firstPageSearch.php" method="post">
		<input id="lat" type="hidden" name="lat" placeholder="" >
		<input id="long" type="hidden" name="long" placeholder="" >
		
		<input id="c"  name="locat" type="submit" value="Current location">
	</form>
	
	
		
	
	<div id="bottomtext">  
		<p> Search over 2500 Gyms by Country, City or Name <p>
	
	</div>
	
	
 </body>
 <script>

 
 
 
 
var x = document.getElementById("demo");
getLocation();
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser. PLease enter a location";
    }
}
function showPosition(position) {
    document.getElementById("lat").value =  position.coords.latitude ;
	document.getElementById("long").value =  position.coords.longitude ;
	
}

</script>

</html>