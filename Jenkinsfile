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
                sh 'pip install playwright'
                sh 'playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m pytest tests/'
            }
        }
    }

    post {
        always {
            junit 'test-results/**/*.xml'
        }
    }
}
