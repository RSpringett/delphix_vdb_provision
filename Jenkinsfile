pipeline { 
    agent any 
    stages { 
        stage('Git Checkout') { 
            steps { 
                echo "Checking out Git repo";
            }
        } 
        
        stage('Get parameters') { 
            steps { 
                echo "Getting vdb parameter details"; 
            } 
        } 
        
        stage('Provision VDB') { 
            steps {
                echo "Provisioning VDB"; 
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