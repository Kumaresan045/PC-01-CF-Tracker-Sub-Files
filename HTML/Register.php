<?php
// database connection code
// $con = mysqli_connect('localhost', 'database_user', 'database_password','database');

$con = mysqli_connect('localhost', 'root', '','storedb');

// get the post records
$name = $_POST['name'];
$city = $_POST['city'];
$age = $_POST['age'];
$phno = $_POST['phno'];

// database insert SQL code
$sql = "INSERT INTO `myguests` (`name`, `city`, `age`, `phno`) VALUES ('$name', '$city', '$age', '$phno')";

// insert in database 
$rs = mysqli_query($con, $sql);

if($rs)
{
	echo "Data Submitted Succesfully!!!";
}
else 
{
	echo "Error: " . $sql . "<br>" . $con->error;
}
  
  $con->close();

?>