pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
		sh 'echo 'Installing required packages ncclient, pandas, ipaddress, netaddr, prettytable''
		sh 'python3 -m pip install ncclient'	 
		sh 'python3 -m pip install pandas'	 
		sh 'python3 -m pip install ipaddress'	 
		sh 'python3 -m pip install netaddr'	 
		sh 'python3 -m pip install prettytable'	 
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
		echo 'Test2'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
