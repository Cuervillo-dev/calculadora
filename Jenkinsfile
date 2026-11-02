pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest -v'
            }
        }

        stage('Deploy') {
            when { branch 'main' }
            steps {
                echo 'Pruebas OK en main: aquí iría el despliegue'
            }
        }
    }

    post {
        success { echo 'Pipeline OK' }
        failure { echo 'Pipeline FALLÓ: revisa el test en rojo' }
    }
}
printf '__pycache__/\n*.pyc\n' > .gitignore
