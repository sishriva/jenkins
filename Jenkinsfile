pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
		echo 'Installing required packages ncclient, pandas, ipaddress, netaddr, prettytable'
		sh 'pip install --upgrade pip'
		sh 'pip install ncclient'	 
		sh 'pip install pandas'	 
		sh 'pip install ipaddress'	 
		sh 'pip install netaddr'	 
		sh 'pip install prettytable'	 
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
