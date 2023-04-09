pipeline {
    agent any

    stages {
        stage('Install required packages') {
            steps {
		echo 'Installing required packages ncclient, pandas, ipaddress, netaddr, prettytable'
		sh 'sudo pip install ncclient'	 
		sh 'sudo pip install pandas'	 
		sh 'sudo pip install ipaddress'	 
		sh 'sudo pip install netaddr'	 
		sh 'sudo pip install prettytable'	 	 
            }
        }
        stage('Check code style') {
            steps {
                echo 'Checking code PEP8 code style'
		sh 'sudo pylint /home/netman/Documents/Lab9/netman_netconf_obj2.py'
//		sh 'cat /home/netman/Documents/Lab9/netman_netconf_obj2.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
