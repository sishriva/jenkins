pipeline {
    agent any

    stages {
        stage('Install required packages') {
            steps {
		echo 'Installing required packages ncclient, pandas, ipaddress, netaddr, prettytable'
		sh 'python3 -m pip install --upgrade pip'
		sh 'python3 -m pip install ncclient'	 
		sh 'python3 -m pip install pandas'	 
		sh 'python3 -m pip install ipaddress'	 
		sh 'python3 -m pip install netaddr'	 
		sh 'python3 -m pip install prettytable'	 
            }
        }
        stage('Check code style') {
            steps {
                echo 'Checking code PEP8 code style'
		sh 'pylint /home/netman/Documents/Lab9/netman_netconf_obj2.py'
//		sh 'cat /home/netman/Documents/Lab9/netman_netconf_obj2.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
		sh 'python3 /home/netman/Documents/Lab9/netman_netconf_obj2.py'
            }
        }
    }
}
