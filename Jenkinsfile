pipeline {
  agent {
    kubernetes {
      yaml '''
spec:
  containers:
  - name: python
    image: python:latest
    command:
    - sleep
    - 99d
  terminationGracePeriodSeconds: 3
      '''
      defaultContainer 'python'
      retries 2
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python helloworld.py'
      }
    }
  }
}