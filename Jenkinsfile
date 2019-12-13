pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python helloworld.py'
            }
        }
    }
}