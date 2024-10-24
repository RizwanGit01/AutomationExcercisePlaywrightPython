pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Environment Info') {
            steps {
                bat 'echo %PATH%'
                bat 'where python || echo Python not found in PATH'
                bat 'dir "C:\\Program Files\\Python*" || echo No Python installation found in Program Files'
                bat 'dir "C:\\Python*" || echo No Python installation found in C:\\'
            }
        }

        stage('Setup') {
            steps {
                script {
                    def pythonPaths = [
                        'C:\\Python311\\python.exe',
                        'C:\\Python310\\python.exe',
                        'C:\\Python39\\python.exe',
                        'C:\\Python38\\python.exe',
                        'C:\\Program Files\\Python311\\python.exe',
                        'C:\\Program Files\\Python310\\python.exe',
                        'C:\\Program Files\\Python39\\python.exe',
                        'C:\\Program Files\\Python38\\python.exe'
                    ]
                    
                    def pythonExe = ''
                    for (path in pythonPaths) {
                        if (fileExists(path)) {
                            pythonExe = path
                            break
                        }
                    }
                    
                    if (pythonExe) {
                        bat "\"${pythonExe}\" -m pip install playwright"
                        bat "\"${pythonExe}\" -m playwright install"
                    } else {
                        error "Python not found. Please install Python or add it to PATH."
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (pythonExe) {
                        bat "\"${pythonExe}\" -m pytest tests/ --junitxml=test-results/results.xml"
                    }
                }
            }
        }
    }

    post {
        always {
            junit 'test-results/results.xml'
        }
    }
}
