#!/bin/bash

NAME=$1
groupReference=$2
dSourceReference=$3 
instanceReference=$4
dxEngineAddress=$5

curl -s -X POST -k --data @- http://${dxEngineAddress}/resources/json/delphix/database/provision -b "cookies.txt" -H "Content-Type: application/json"<<EOF
{
    "type": "MSSqlProvisionParameters",
    "container": {
        "type": "MSSqlDatabaseContainer",
        "name": "${NAME}",
        "group": "${groupReference}",
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
        "repository": "${instanceReference}",
        "databaseName": "${NAME}",
        "recoveryModel": "SIMPLE",
        "mirroringState": "NONE"
    },
    "timeflowPointParameters": {
        "type": "TimeflowPointSemantic",
        "location": "LATEST_SNAPSHOT",
        "container": "${dSourceReference}"
    },
    "masked": false
}
EOF 

