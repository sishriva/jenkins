pipeline {
    agent any

    stages {
        stage('Install required packages') {
            steps {
		echo 'Installing required packages ncclient, pandas, ipaddress, netaddr, prettytable'
		sh 'pip3 install ncclient'	 
		sh 'pip3 install pandas'	 
		sh 'pip3 install ipaddress'	 
		sh 'pip3 install netaddr'	 
		sh 'pip3 install prettytable'	 
		sh 'pip3 install pylint'	 
            }
        }
        stage('Check code style') {
            steps {
                echo 'Checking code PEP8 code style'
		sh '/home/netman/.local/bin/pylint /home/netman/Documents/Lab9/netman_netconf_obj2.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
