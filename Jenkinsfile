pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\Program Files\\Python312'
        PATH = "${PYTHON_HOME};${PYTHON_HOME}\\Scripts;${env.PATH}"
    }

    stages {

        stage('Run Selenium Tests with pytest') {
            steps {
                echo "Running Selenium Tests using pytest"
                bat 'python -m pip install -r requirements.txt'
                bat 'start /B python app.py'
                bat 'ping 127.0.0.1 -n 5 > nul'
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                bat "docker build -t seleniumdemoapp:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                  usernameVariable: 'DOCKER_USER',
                                                  passwordVariable: 'DOCKER_PASS')]) {
                    bat 'echo %DOCKER_PASS%| docker login -u %DOCKER_USER% --password-stdin'
                }
            }
        }

        stage('push Docker Image to Docker Hub') {
            steps {
                echo "push Docker Image to Docker Hub"
                bat "docker tag seleniumdemoapp:v1 likithavajinepalli/sample2026:seleniumtestimage"
                bat "docker push likithavajinepalli/sample2026:seleniumtestimage"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}