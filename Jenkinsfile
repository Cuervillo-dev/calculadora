pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest -v'
            }
        }

        stage('Aprobación') {
            steps {
                input message: '¿Desplegar a producción?', ok: 'Desplegar'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Pruebas OK y aprobado: aquí iría el despliegue'
            }
        }
    }

    post {
        success { echo 'Pipeline OK' }
        failure { echo 'Pipeline FALLÓ: revisa el test en rojo' }
    }
}
