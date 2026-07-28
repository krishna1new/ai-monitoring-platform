pipeline {
    agent any

    environment {
        IMAGE_NAME = "ai-monitoring-platform"
        CONTAINER_NAME = "ai-monitoring-container"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build --no-cache -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f $CONTAINER_NAME || true'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker run -d \
                    --name $CONTAINER_NAME \
                    --restart unless-stopped \
                    -p 8000:8000 \
                    $IMAGE_NAME
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 10'
                sh 'curl http://localhost:8000/docs'
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }

        failure {
            echo 'Deployment Failed!'
        }
    }
}
