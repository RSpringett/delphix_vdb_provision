import os
import json 
import sys 

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


if __name__ == "__main__": 
    print("Logging in")
    os.system("sh login.sh")

    groupName = sys.argv[1] 
    sourceName = sys.argv[2] 

    groupReference = getGroupReferenceID(groupName)
    dSourceReference = getdSourceContainerID(sourceName)
    with open("configFile.txt", "w") as configFile: 
        configFile.write(f"{groupReference}\n{dSourceReference}")
        


