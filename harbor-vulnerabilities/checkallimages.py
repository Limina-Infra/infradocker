import json
import sys
import pip._vendor.requests as requests

if len(sys.argv)<4:
    raise Exception('Script need the following args: registry_url, name of projects, and the token')

registry_url = str(sys.argv[1])
projects = sys.argv[2].split(',')
token = str(sys.argv[3])
conditions = None
try:
    conditions = list(map(lambda x: int(x),sys.argv[4].split(',')))
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

header = {'Authorization': 'Basic ' + token}
errormsg=False
msg=""

for x in range(len(projects)):
    url = "https://"+registry_url+"/api/projects?name="+projects[x]
    r = requests.get(url, headers=header)
    data_project = r.json()
    project_id = str(data_project[0]['project_id'])

    url="https://"+registry_url+"/api/repositories?project_id="+project_id+"&page_size=100"
    r = requests.get(url, headers=header)
    images = r.json()

    for image in images:
        image_name=image['name'].replace("/","%2F")
        url = "https://"+registry_url+"/api/repositories/"+image_name+"/tags"
        r = requests.get(url, headers=header)
        tags = r.json()
        for tag in tags:
            breach_limit = False
            tag_name = tag['name']
            image_link = "https://"+registry_url+"/harbor/projects/"+project_id+"/repositories/"+image_name+"/tags/"+tag_name
            scanner = tag['scan_overview']['application/vnd.scanner.adapter.vuln.report.harbor+json; version=1.0']
            if scanner['scan_status']=="Success":
                results = scanner['summary']['summary']
                for key in results.keys():
                    if vulnerabilities.get(key) != -1:
                        if results[key] >= vulnerabilities.get(key) :
                            if not breach_limit:
                                breach_limit = True
                                msg += "\r\n"+image_link+"\r\n"
                            msg += key+": "+str(results[key])+" | "
                            
print(msg)
if msg != "":
    sys.exit(1)



