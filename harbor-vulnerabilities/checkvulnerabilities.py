import json
import requests
import sys

if len(sys.argv)<6:
    raise Exception('Script need the following args: registry_url, name of project, image, tag, and the token')

registry_url = str(sys.argv[1])
project = str(sys.argv[2])
image = str(sys.argv[3])
tag = str(sys.argv[4])
token = str(sys.argv[5])
conditions = None
try:
    conditions = list(map(lambda x: int(x),sys.argv[6].split(',')))
    conditions.insert(0,-1)
except IndexError:
    conditions = [-1, -1, -1, -1, -1]

url = "https://"+registry_url+"/api/repositories/"+project+"%2F"+image+"/tags"
header = {'Authorization': 'Basic ' + token}
r = requests.get(url, headers=header)
tags = r.json()

for obj in tags:
    if obj['name']==tag:
        url = "https://"+registry_url+"/api/projects?name="+project
        r = requests.get(url, headers=header)
        data_project = r.json()
        project_id = str(data_project[0]['project_id'])
        image_link = "https://"+registry_url+"/harbor/projects/"+project_id+"/repositories/"+project+"%2F"+image+"/tags/"+tag

        vName = ["Negligible", "Unknown", "Low", "Medium", "High"]
        vulnerabilities = [0,0,0,0,0]
        for summary in obj['scan_overview']['components']['summary']:
            vulnerabilities[int(summary['severity'])-1]=int(summary["count"])

        error=False
        for i in range(len(vName)):
            msg=vName[i]+": "+str(vulnerabilities[i])
            if conditions[i] != -1:
                if vulnerabilities[i] < conditions[i]:
                    msg+=" < "+str(conditions[i])
                else:
                    msg+=" >= "+str(conditions[i])+" BREACH OF CONDITION"
                    error=True
            print(msg)
        print("For more informations about the vulnerabilities, please check at: "+image_link)
        if error:
            raise Exception('Container contains too much vulnerabilities')

        sys.exit(0)

raise Exception('Image not found')
