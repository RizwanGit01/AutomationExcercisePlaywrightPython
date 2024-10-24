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
                bat 'pip install playwright'
                bat 'playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest tests/'
            }
        }
    }

    post {
        always {
            junit 'test-results/**/*.xml'
        }
    }
}
