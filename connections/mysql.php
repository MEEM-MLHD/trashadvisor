<?php
	// On d�finit les 4 variables n�cessaires � la connexion MySQL :
	$hostname = "XXXX";
	$user     = "XXXX";
	$pdbd = "XXXXX";
	$nom_base_donnees = "XXXXXX";

	// Connexion au serveur MySQL

	$mysqli = mysqli_connect($hostname, $user, $pdbd, $nom_base_donnees);
	
	if (mysqli_connect_errno($mysqli)) 
	{
    			echo "Echec lors de la connexion � MySQL : " . mysqli_connect_error();
	}

?>