import json
import sys
import pip._vendor.requests as requests

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
except IndexError:
    conditions = [-1, -1, -1, -1, -1, -1]

vulnerabilities = {
    "Critical": conditions[0],
    "High": conditions[1],
    "Medium": conditions[2],
    "Low": conditions[3],
    "Negligible": conditions[4],
    "Unknown": conditions[5]
}

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
        scanner = obj['scan_overview']['application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0']
        error=False
        if scanner['scan_status']=="Success":
            results = scanner['summary']['summary']
            for key in results.keys():
                msg=key+": "+str(results[key])
                if vulnerabilities.get(key) != -1:
                    if results[key] < vulnerabilities.get(key) :
                        msg+=" < "+str(vulnerabilities.get(key))
                    else: 
                        msg+=" >= "+str(vulnerabilities.get(key))+" BREACH OF CONDITION"
                        error=True
                print(msg)
        print("For more informations about the vulnerabilities, please check at: "+image_link)
        if error:
            sys.exit(1)
        sys.exit(0)
