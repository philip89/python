<?php

$countyv = $_POST['countyBar'];
 
// echo $countyv;
//$mycounty = fopen("county.txt", "w") or die("Unable to open file!");

//fwrite($mycounty, $countyv);
/// This is setting up a sesion with list page and passsing the county in so that the county can be used with list page to create thirdPage with new reviews on it
session_start();
	$_SESSION['county'] = $countyv;

///
sleep(2);
shell_exec("sudo python3 reviewsPage.py .$countyv");
//echo shell_exec("sudo python3 reviewsPage.py .$countyv 2>&1");
 
header("Refresh:2000; url=thirdPage.html");
header("Location: thirdPage.html");
 
?> 
