import sys
import os


NAME = "tryingAgain"


openBracket ='{'
closeBracket = '}'

json = f"""{openBracket}
"type": "MSSqlProvisionParameters", 
    "container": {openBracket}
        "type": "MSSqlDatabaseContainer", 
        "name": "{NAME}",
        "group": "GROUP-21", 
        "sourcingPolicy": {openBracket} 
            "type": "SourcingPolicy", 
            "logsyncEnabled": false
        {closeBracket}
    {closeBracket},
    "source": {openBracket}
        "type": "MSSqlVirtualSource", 
        "operations": {openBracket} 
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
        {closeBracket},
        "allowAutoVDBRestartOnHostReboot": true, 
        "enableCdcOnProvision": false
    {closeBracket}, 
    "sourceConfig": {openBracket}
        "type": "MSSqlSIConfig", 
        "linkingEnabled": false, 
        "repository": "MSSQL_INSTANCE-1", 
        "databaseName": "{NAME}", 
        "recoveryModel": "SIMPLE", 
        "mirroringState": "NONE"
    {closeBracket}, 
    "timeflowPointParameters": {openBracket} 
        "type": "TimeflowPointSemantic", 
        "location": "LATEST_SNAPSHOT", 
        "container": "MSSQL_DB_CONTAINER-117"
    {closeBracket}, 
    "masked": false
{closeBracket}"""

if __name__ == "__main__": 
    os.system(f"""curl -s -X POST -k --data @- http://10.44.1.160/resources/json/delphix/database/provision -b "cookies.txt" -H "Content-Type: application/json"<<EOF
    {json}""")

