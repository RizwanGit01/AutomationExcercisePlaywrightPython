pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                bat 'C:\\Path\\To\\Python\\python.exe -m pip install playwright'
                bat 'C:\\Path\\To\\Python\\python.exe -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'C:\\Path\\To\\Python\\python.exe -m pytest tests/'
            }
        }
    }

    post {
        always {
            junit 'test-results/**/*.xml'
        }
    }
}
