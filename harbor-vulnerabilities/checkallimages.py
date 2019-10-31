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
    conditions = [-1, -1, -1, -1]

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
            vulnerabilities = [0,0,0,0,0]
            tag_name = tag['name']
            image_link = "https://"+registry_url+"/harbor/projects/"+project_id+"/repositories/"+image_name+"/tags/"+tag_name
            for obj in tag['scan_overview']['components']['summary']:
                vulnerabilities[int(obj['severity'])-1]=int(obj["count"])
 
            #2-Unknown, 3-Low, 4-Medium, 5-High
            vName=["Unknown","Low","Medium","High"]
            adderror=False
            for i in range(len(vName)):
                if conditions[i] != -1:
                    if vulnerabilities[i+1] >= conditions[i]:
                        if not adderror:
                            msg += "\r\n"+image_link+"\r\n"
                            adderror=True
                            errormsg = True
                        msg += vName[i]+": "+str(vulnerabilities[i+1])+" | "
print(msg)
if errormsg:
    sys.exit(1)



