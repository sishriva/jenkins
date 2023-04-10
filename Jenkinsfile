pipeline {
    agent any

    stages {
        stage('Install required packages') {
            steps {
		echo 'Installing required packages ncclient, pandas, ipaddress, netaddr, prettytable....'
		sh 'python3 -m pip install --upgrade pip'
		sh 'python3 -m pip install ncclient'	 
		sh 'python3 -m pip install pandas'	 
		sh 'python3 -m pip install ipaddress'	 
		sh 'python3 -m pip install netaddr'	 
		sh 'python3 -m pip install prettytable'	 
		sh 'python3 -m pip install netmiko==3.0.0'	 
		sh 'python3 -m pip install pylint==2.9.6'	 
            }
        }
        stage('Check code style') {
            steps {
                echo 'Checking code PEP8 code style....'
		sh 'sudo /home/netman/.local/bin/pylint /home/netman/Documents/Lab9/netman_netconf_obj2.py'
//		sh 'cat /home/netman/Documents/Lab9/netman_netconf_obj2.py'
            }
        }
        stage('Push the configuration') {
            steps {
                echo 'Pushing the configuration on routers....'
		sh 'python3 /home/netman/Documents/Lab9/netman_netconf_obj2.py'
            }
	}
        stage('Unit Testing') {
            steps {
                echo 'Unit Testing....'
		sh 'python3 /home/netman/Documents/Lab9/unitest.py'
            }
        }
    }
    post {
        always {   
            emailext attachLog: true, body: ' Project: "$PROJECT_NAME", Build Number: "$BUILD_NUMBER", Build Status: "$BUILD_STATUS" \nFor detailed report please open the attached detailed report file.', subject: '$PROJECT_NAME, $BUILD_NUMBER, $BUILD_STATUS', to: 'siddharth.s2295@gmail.com'
        }
    }
}
