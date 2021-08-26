pipeline {
    agent { label "test71" }
	parameters {
		string(name: 'slave', defaultValue: '3', description: '请输入需要启动的slave个数(整数)')
	}
    stages { 
        stage('Compose_Down') {
            steps {
				sh "docker-compose down -v"
            }
        }
		
        stage('Docker_Build') {
            steps {
				sh "docker build -t jimmy_locust ."
            }
        }
        
        stage('Compose_Up') {
            steps {
				sh "docker-compose up -d --scale worker=${params.slave}"
            }
        }
    }
}