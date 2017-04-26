<?php

$search = $_POST['search'];
$lat = $_POST['lat'];
$long = $_POST['long'];
 

if (isset($search)){
	
	shell_exec("python3 searchFoliumCreator.py " .$search);

	session_start();
	$_SESSION['firstMessage'] = $search;

}else{
	
	shell_exec("python3 currentLocationFoliumMaker.py " .$lat .$long);

	session_start();
	$_SESSION['firstMessage'] = 'your location';

}
 
header("Refresh:2000; url=mymap2.html");
sleep(1);
header("Refresh:2000; url=secondPage.php");
header("Location: secondPage.php");
 


?> 
