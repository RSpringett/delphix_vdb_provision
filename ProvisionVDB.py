import sys
import os
import time
from http.cookiejar import MozillaCookieJar
import requests

NAME = sys.argv[1]
groupReference = sys.argv[2] 
dSourceReference = sys.argv[3] 

# openBracket ='{'
# closeBracket = '}'

# json = f"""{openBracket}
# "type": "MSSqlProvisionParameters", 
#     "container": {openBracket}
#         "type": "MSSqlDatabaseContainer", 
#         "name": "{NAME}",
#         "group": "{groupReference}", 
#         "sourcingPolicy": {openBracket} 
#             "type": "SourcingPolicy", 
#             "logsyncEnabled": false
#         {closeBracket}
#     {closeBracket},
#     "source": {openBracket}
#         "type": "MSSqlVirtualSource", 
#         "operations": {openBracket} 
#             "type": "VirtualSourceOperations", 
#             "configureClone": [], 
#             "preRefresh": [], 
#             "postRefresh": [], 
#             "preRollback": [], 
#             "postRollback": [], 
#             "preSnapshot": [], 
#             "postSnapshot": [], 
#             "preStart": [], 
#             "postStart": [], 
#             "preStop": [], 
#             "postStop": []
#         {closeBracket},
#         "allowAutoVDBRestartOnHostReboot": true, 
#         "enableCdcOnProvision": false
#     {closeBracket}, 
#     "sourceConfig": {openBracket}
#         "type": "MSSqlSIConfig", 
#         "linkingEnabled": false, 
#         "repository": "MSSQL_INSTANCE-1", 
#         "databaseName": "{NAME}", 
#         "recoveryModel": "SIMPLE", 
#         "mirroringState": "NONE"
#     {closeBracket}, 
#     "timeflowPointParameters": {openBracket} 
#         "type": "TimeflowPointSemantic", 
#         "location": "LATEST_SNAPSHOT",
#         "container": "{dSourceReference}"
#     {closeBracket}, 
#     "masked": false
# {closeBracket}"""

if __name__ == "__main__": 
    
    os.system(f"sh curlCommand.sh {NAME} {groupReference} {dSourceReference}")
        
    # os.system(f'curl -s -X POST -k --data @- http://10.44.1.160/resources/json/delphix/database/provision -b "cookies.txt" -H "Content-Type: application/json"<<EOF\n{json}\nEOF')
    # time.sleep(10)
    # print("onto the next!")
    # print(json)

    print("actually doing something... ")
