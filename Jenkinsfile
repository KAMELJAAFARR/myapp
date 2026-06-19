pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Python application...'
                sh 'python3 --version'
		sh 'python3 app.py'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'pip3 install pytest --break-system-packages'
                sh 'python3 -m pytest -v'
            }
        }

        stage('Package Application') {
            steps {
                echo 'Packaging application...'
                sh 'mkdir -p package'
                sh 'cp app.py requirements.txt package/'
                sh 'tar -czf myapp.tar.gz package'
            }
        }

        stage('Deploy to Test') {
            steps {
                echo 'Deploying to test environment...'
                sh 'mkdir -p /tmp/test-environment'
                sh 'cp myapp.tar.gz /tmp/test-environment/'
            }
        }

        stage('Manual Approval') {
            steps {
                input message: 'Approve deployment to production?', ok: 'Deploy'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying to production environment...'
                sh 'mkdir -p /tmp/production-environment'
                sh 'cp myapp.tar.gz /tmp/production-environment/'
            }
        }
    }
}
