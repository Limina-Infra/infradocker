import json
import sys
import pip._vendor.requests as requests

if len(sys.argv)<4:
    raise Exception('Script need the following args: registry_url, name of projects, and the token')

registry_url = str(sys.argv[1])
projects = sys.argv[2].split(',')
token = str(sys.argv[3])

header = {'Authorization': 'Basic ' + token}
errormsg=False
count = 0
for x in range(len(projects)):
    url = "https://"+registry_url+"/api/projects?name="+projects[x]
    r = requests.get(url, headers=header)
    data_project = r.json()
    project_id = str(data_project[0]['project_id'])

    url="https://"+registry_url+"/api/repositories?project_id="+project_id+"&page_size=100"
    r = requests.get(url, headers=header)
    images = r.json()

    for image in images:
        image_name=image['name']
        url = "https://"+registry_url+"/api/repositories/"+image_name+"/tags"
        r = requests.get(url, headers=header)
        tags = r.json()

        for tag in tags:
            count += 1
            tag_name = tag['name']
            image_link = "https://"+registry_url+"/harbor/projects/"+project_id+"/repositories/"+image_name+"/tags/"+tag_name
            print(registry_url+"/"+image_name+":"+tag_name)
 
print("total images : "+ str(count))
if errormsg:
    sys.exit(1)
