<?php
$s  = $_POST['listSearch'];// this is the gym name
$c = $_POST['placeidSearch'];// this is the gym id
 
 
$myfile = fopen("placeIdforThirdPage.txt", "w") or die("Unable to open file!");

fwrite($myfile, $c);

///// This is taking the county name passed by the county page to that it can be used to create new thirdPage with sys.argv[1]
session_start();

$county = $_SESSION['county'];

/////
$co = "kilkenny";
//sleep(.5);
//exec("python3 firstDatebaseTest.py");
//sleep(.5);
//exec("python3 graphMakingProgram.py");
sleep(.5);

//////// This is determining if a person clicked the search button without a county name in it
///if they did the default county will show which is set to kilkenny above
if (empty($county)){
	//echo $co;
exec("python3 reviewsPage.py .$co");
	//exec("python3 reviewsPage.py .$co");
}else{
//echo $county; exec("python3 reviewsPage.py .$county");
exec("python3 reviewsPage.py .$county");
}
	//}
////////

//exec("python reviewsPage.py .$county");
sleep(.5);
// echo($s);
 //echo($c);
header("Refresh:2000; url=thirdPage.html");
header("Location: thirdPage.html");
?> 