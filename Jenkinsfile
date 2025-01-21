pipeline {
    agent any
    
   stages {
        stage('git checkout') {
            steps {
                git 'https://github.com/rajdeepsingh642/python-app.git'
            }
        }
        stage('build image') {
            steps {
             sh "docker build -t radeepsingh642/python-app:$BUILD_NUMBER ."
             }
        }    
        stage('docker run') {
            steps {
             sh "docker run -d -p 5000:5000 radeepsingh642/python-app:$BUILD_NUMBER"
             }
        }     
   }   

}