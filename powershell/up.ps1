function up($number){
	if(!$number){
		cd ..
	}
	elseif($number -match "^[0-9]*$"){
		for($i = 1; $i -le $number; $i++){
			cd ..
		}
	}
	else{
		write-host "No number given"
		write-host "Usage - up [numberOfCDs]"
	}
}
