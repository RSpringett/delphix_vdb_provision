properties([parameters([string('groupName'), string('sourceName')])])
pipeline { 
    agent any 
    stages { 
        stage('Git Checkout') {
            steps {
                sh 'rmdir /s /q delphix_vdb_provision';
                sh 'git clone https://github.com/cameronbose/delphix_vdb_provision.git';
            }
        }
        
        stage('Get parameters') { 
            steps { 
                sh "python getParameters.py ${params.groupName} ${params.sourceName}";
            }
        } 
        
        stage('Provision VDB') { 
            steps {
                echo "Provisioning VDB";
                sh 'python start.py' 
            }
        }
    }
    post { 
        always { 
            echo "this will always run!"; 
        }
        success { 
            echo "VDB successfully Provisioned!"; 
        } 
        failure { 
            echo "VDB provisioning has failed - please look at the error logs."; 
        } 
        unstable { 
            echo "Jenkins run was unstable, please check logs."; 
        } 
        changed { 
            echo "VDB provisioning is now successful!"; 
            
        }
    }
}
