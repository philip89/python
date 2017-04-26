<?php
 $s  = $_POST['search'];

// Executes the python script to create a new map of the place the user passed in
shell_exec("python3 searchFoliumCreator.py " .$s);

// This is a session created so that the name of the place the user entered in the search bar can be displayed on the webpage
session_start();
$_SESSION['firstMessage'] = $s;
/////////////

// This is refreshing the map to make sure it is of the correct location
header("Refresh:2000; url=mymap2.html");
sleep(1);


// Refreshing the page so the new map is on it
header("Refresh:2000; url=secondPage.php");

// Redirecting to the webpage
header("Location: secondPage.php");

 

?> 