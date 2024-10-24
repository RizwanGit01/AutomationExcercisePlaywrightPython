pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Find Python') {
            steps {
                bat 'where python'
            }
        }

        stage('Setup') {
            steps {
                bat 'python -m pip install playwright'
                bat 'python -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest tests/ --junitxml=test-results/results.xml'
            }
        }
    }

    post {
        always {
            junit 'test-results/results.xml'
        }
    }
}
