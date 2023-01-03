import time 
import os

configFile = open("configFile.txt", "r").read().splitlines()
configList = [i.strip() for i in configFile]
groupReference = configList[0]
dSourceReference = configList[1]
environmentInstanceReference = configList[2]

vdbFile = open("vdbNames.txt", "r").read().splitlines()
vdbList = [i.strip() for i in vdbFile]

if __name__ == "__main__": 
    
    for vdbName in vdbList: 
        os.system(f"sh curlCommand.sh {vdbName} {groupReference} {dSourceReference} {environmentInstanceReference}")
        time.sleep(60)

    # for vdb in vdbList: 
    #     print("about to...")
    #     os.system(f"python3 ProvisionVDB.py {vdb}")
    #     time.sleep(60)
    #     print("finished...")


    # 1). Login 
    # 2). getParameters python file -> get source & group referenceID 
    # 3). 
