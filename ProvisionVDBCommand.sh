#!/bin/bash
pwd
NAME=$1

#curl -s -X POST -k --data @- http://10.44.1.160/resources/json/delphix/database/provision -b "cookies.txt" -H "Content-Type: application/json"<<EOF
json='{
    "type": "MSSqlProvisionParameters", 
    "container": {
        "type": "MSSqlDatabaseContainer", 
        "name": \""$NAME"\",
        "group": "GROUP-21", 
        "sourcingPolicy": { 
            "type": "SourcingPolicy", 
            "logsyncEnabled": false
        }
    },
    "source": {
        "type": "MSSqlVirtualSource", 
        "operations": { 
            "type": "VirtualSourceOperations", 
            "configureClone": [], 
            "preRefresh": [], 
            "postRefresh": [], 
            "preRollback": [], 
            "postRollback": [], 
            "preSnapshot": [], 
            "postSnapshot": [], 
            "preStart": [], 
            "postStart": [], 
            "preStop": [], 
            "postStop": []
        },
        "allowAutoVDBRestartOnHostReboot": true, 
        "enableCdcOnProvision": false
    }, 
    "sourceConfig": {
        "type": "MSSqlSIConfig", 
        "linkingEnabled": false, 
        "repository": "MSSQL_INSTANCE-1", 
        "databaseName": \""${NAME}"\", 
        "recoveryModel": "SIMPLE", 
        "mirroringState": "NONE"
    }, 
    "timeflowPointParameters": { 
        "type": "TimeflowPointSemantic", 
        "location": "LATEST_SNAPSHOT", 
        "container": "MSSQL_DB_CONTAINER-117"
    }, 
    "masked": false
}'
#EOF
echo ${json} 
