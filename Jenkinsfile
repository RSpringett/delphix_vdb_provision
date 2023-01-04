properties([parameters([choice(choices: ['MgtAppServer', 'SQL2019_Source', 'SQL2019_Target', 'linuxsource', 'linuxtarget'], name: 'Environment'), choice(choices: ['MSSQLSERVER', 'SQLEXPRESS', 'Unstructured Files'], name: 'environmentInstance'), choice(choices: ['6.0.14.0', '6.0.15.0', '6.0.16.0', '6.0.17.0'], name: 'dxVersion'), string(name: 'password', trim: true), string(name: 'groupName', trim: true), string(name: 'sourceName', trim: true), string(defaultValue: 'admin', name: 'username', trim: true), string(defaultValue: '10.44.1.160', name: 'dxEngineAddress', trim: true)])])
pipeline { 
    agent any 
    stages { 
        stage('Git Checkout') {
            steps {
                bat 'rmdir /s /q delphix_vdb_provision';
                bat 'git clone https://github.com/cameronbose/delphix_vdb_provision.git';
            }
        }
        
        stage('Get parameters') { 
            steps { 
                bat "python getParameters.py ${params.groupName} ${params.sourceName} ${params.Environment} ${params.environmentInstance} ${params.username} ${params.password} ${params.dxEngineAddress} ${params.dxVersion}";
            }
        } 
        
        stage('Provision VDB') { 
            steps {
                echo "Provisioning VDB";
                bat 'python start.py' 
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

