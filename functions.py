import os
import json 

def getGroupReferenceID(groupName):
    APIQuery = os.popen('curl -X GET -k http://10.44.1.160/resources/json/delphix/group -b "cookies.txt" -H "Content-Type: application/json"').read()
    queryDict = json.loads(APIQuery)
    for group in queryDict["result"]:
        if group['name'] == groupName: 
            groupReference = group['reference']
            print(f"Name: {groupName}, Reference: {group['reference']}")
    
    return groupReference

def getdSourceContainerID(dSourceName): 
    APIQuery = os.popen('curl -X GET -k http://10.44.1.160/resources/json/delphix/database -b "cookies.txt" -H "Content-Type: application/json"').read()
    queryDict = json.loads(APIQuery) 
    for db in queryDict["result"]:
        if db['name'] == dSourceName: 
            dSourceContainer = db['reference']
            print(f"this is it ****************************{dSourceContainer}***************************")

    #can i use walrus operator here? 
    return dSourceContainer

def provisionVDB(vdbName, groupReference, dSourceContainer): 
    print("HELLOOO")
    openBracket ='{'
    closeBracket = '}'
    json = f"""{openBracket}
    "type": "MSSqlProvisionParameters", 
        "container": {openBracket}
            "type": "MSSqlDatabaseContainer", 
            "name": "{vdbName}",
            "group": "{groupReference}", 
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
            "databaseName": "{vdbName}", 
            "recoveryModel": "SIMPLE", 
            "mirroringState": "NONE"
        {closeBracket}, 
        "timeflowPointParameters": {openBracket} 
            "type": "TimeflowPointSemantic", 
            "location": "LATEST_SNAPSHOT", 
            "container": "{dSourceContainer}"
        {closeBracket}, 
        "masked": false
    {closeBracket}"""
    print(json)
    os.system(f"""curl -s -X POST -k --data @- http://10.44.1.160/resources/json/delphix/database/provision -b "cookies.txt" -H "Content-Type: application/json"<<EOF
    {json}""")
    print("done this bit!")