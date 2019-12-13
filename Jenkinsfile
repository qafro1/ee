pipeline {
    agent { docker { image 'python:latest' } }
    stages {
        stage('build') {
            steps {
                sh 'python helloworld.py'
            }
        }
    }
}