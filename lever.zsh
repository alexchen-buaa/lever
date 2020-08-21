lever(){
	if [[ $# -eq 0 ]]
	then
		python ~/toolbox/lever/lever.py
	elif [ $1 = "pull" ]
	then
		python ~/toolbox/lever/pull.py
	fi
}
