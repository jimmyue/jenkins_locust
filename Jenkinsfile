pipeline {
    agent { label "test71" }
    stages { 
        stage('Compose_Down') {
            steps {
				sh 'docker-compose down -v'
            }
        }
		
        stage('Docker_Build') {
            steps {
				sh 'docker build -t jimmy_locust .'
            }
        }
        
        stage('Compose_Up') {
            steps {
				sh '''
				docker-compose up -d --scale worker=3 
				exit 0
				'''
            }
        }
    }
}