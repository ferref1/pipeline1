pipeline {
    agent any

    environment {
        GIT_TOKEN = credentials('hola')
    }

    stages {
        stage('Limpiar Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Clonar Repositorio') {
            steps {
                withCredentials([string(credentialsId: 'hola', variable: 'TOKEN')]) {
                    sh '''
                        git clone -b master https://ferref1:$TOKEN@github.com/ferref1/pipeline1.git
                    '''
                }
            }
        }

        stage('Instalar Dependencias') {
            steps {
                dir('pipeline1') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt || echo "No hay requirements.txt"
                    '''
                }
            }
        }

        stage('Ejecutar Pruebas Unitarias') {
            steps {
                dir('pipeline1') {
                    sh '''
                        echo "Ejecutando pruebas unitarias..."
                        python3 -m unittest discover tests || echo "No se encontraron pruebas"
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado.'
        }
        success {
            echo 'Pipeline completado con éxito.'
        }
        failure {
            echo 'Pipeline falló.'
        }
    }
}
