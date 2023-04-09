pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
		echo 'Installing required packages ncclient, pandas, ipaddress, netaddr, prettytable'
		sh 'pip3 install --upgrade pip'
		sh 'pip3 install ncclient'	 
		sh 'pip3 install pandas'	 
		sh 'pip3 install ipaddress'	 
		sh 'pip3 install netaddr'	 
		sh 'pip3 install prettytable'	 
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
