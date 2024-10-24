pipeline {
    agent any

    environment {
        PYTHON_PATH = 'C:\\Users\\shaik\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Environment Info') {
            steps {
                bat 'echo %PATH%'
                bat '"${PYTHON_PATH}" --version || echo Python version command failed'
            }
        }

        stage('Setup') {
            steps {
                bat '"${PYTHON_PATH}" -m pip install playwright'
                bat '"${PYTHON_PATH}" -m playwright install'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"${PYTHON_PATH}" -m pytest tests/ --junitxml=test-results/results.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'test-results/results.xml'
        }
    }
}
