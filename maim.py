pipeline script {
    stages{
        stage ('clean')
        steps {
            sh 'mvn clean'
            stage ('test')
            steps {
                sh 'mvn test'
                stage ('build')
                steps {
                    sh 'mvn build'

         } 

            
     }
}  
