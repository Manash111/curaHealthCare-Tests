pipeline {
    agent any

     triggers{
        pollSCM '* * * * *'
    }

    stages {
        stage('Building.......') {
            steps {
                echo 'Install Dependencies'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }
        stage('Testing......') {
            steps {
                echo 'Run Robot Tests'
                bat 'venv\\Scripts\\pip install -e .'
                bat 'venv\\Scripts\\python tests/test_*.py'
            }
        }
    }
//     post {
//
//         always {
//             emailext (
//                 to: "manashmaharjan5@gmail.com",
//                 subject: "Build #${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
//                 body: "Build URL: ${env.BUILD_URL}",
//                 attachmentsPattern: "reports/*.html"
//             )
//         }
//         success {
//             emailext subject: "Build Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
//                      body: "Good news! The Jenkins build succeeded.\n\nCheck console: ${env.BUILD_URL}",
//                      to: 'manashmaharjan5@gmail.com'
//         }
//         failure {
//             emailext subject: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
//                      body: "Oops! The Jenkins build failed.\n\nCheck details: ${env.BUILD_URL}",
//                      to: 'manashmaharjan5@gmail.com'
//         }
//     }
}