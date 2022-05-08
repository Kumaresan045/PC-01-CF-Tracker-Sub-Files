<?php
// database connection code
// $con = mysqli_connect('localhost', 'database_user', 'database_password','database');

$con = mysqli_connect('localhost', 'root', '','storedb');

// get the post records
$name = $_POST['name'];

// database fetch SQL query
$sql = "select * from myguests where name='{$name}';";

// fetch from database 
$rs = mysqli_query($con, $sql);

if($rs)
{
	echo "Data Fetched Successfully!!! <br><br><br>";
	while($row = mysqli_fetch_array($rs, MYSQLI_ASSOC))
	{
		echo   "--------------------------------<br>";
		echo "Name :{$row['name']}  <br> ";
		echo  "City : {$row['city']} <br>";
		echo  "Age : {$row['age']} <br>";
		echo  "Ph.No : {$row['phno']} <br>";
		echo   "--------------------------------<br>";
	 }
}
else 
{
	die('Could not get data: ' . mysql_error());
}
  
  $con->close();

?>