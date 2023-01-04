import os
import json 
import sys 


versionDict = {'6.0.14.0':'1.11.14','6.0.15.0':'1.11.15','6.0.16.0':'1.11.16','6.0.17.0':'1.11.17'}

def getAPIVersion(delphixVersion):
    apiVersion = versionDict[delphixVersion]
    major,minor,micro = apiVersion.split('.')
    return major,minor,micro 

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
    return dSourceContainer

def getTargetEnvironment(environmentName): 
    APIQuery = os.popen('curl -X GET -k http://10.44.1.160/resources/json/delphix/environment -b "cookies.txt" -H "Content-Type: application/json"').read()
    queryDict = json.loads(APIQuery)
    for db in queryDict["result"]:
        if db['name'] == environmentName:
            environmentReference = db['reference']
    return environmentReference

def getEnvironmentInstance(instanceName, environmentReference): 
    APIQuery = os.popen('curl -X GET -k http://10.44.1.160/resources/json/delphix/repository -b "cookies.txt" -H "Content-Type: application/json"').read()
    queryDict = json.loads(APIQuery)
    for db in queryDict["result"]:
        if db['name'] == instanceName and db['environment'] == environmentReference: 
            instanceReference = db['reference']
    return instanceReference


if __name__ == "__main__": 
    
    groupName = sys.argv[1] 
    sourceName = sys.argv[2] 
    environmentName = sys.argv[3]
    environmentInstance = sys.argv[4]
    username = sys.argv[5]
    password = sys.argv[6]
    dxEngineAddress = sys.argv[7]
    delphixVersion = sys.argv[8]

    major,minor,micro = getAPIVersion(delphixVersion)

    print("Logging on --->")
    os.system(f"sh login.sh {username} {password} {dxEngineAddress} {major} {minor} {micro}")

    groupReference = getGroupReferenceID(groupName)
    dSourceReference = getdSourceContainerID(sourceName)
    environmentReference = getTargetEnvironment(environmentName)
    instanceReference = getEnvironmentInstance(environmentInstance, environmentReference)

    with open("configFile.txt", "w") as configFile: 
        configFile.write(f"{groupReference}\n{dSourceReference}\n{instanceReference}\n{dxEngineAddress}")

