import json
import requests
import sys

if len(sys.argv)!=6:
    raise Exception('Script need the following args : registry_url, name of the repo, image, tag, and the token')

registry_url = str(sys.argv[1])
repository_name = str(sys.argv[2])
image = str(sys.argv[3])
tag = str(sys.argv[4])
token = str(sys.argv[5])

url = "https://"+registry_url+"/api/repositories/"+repository_name+"%2F"+image+"/tags/"+tag+"/vulnerability/details"

header = {'Authorization': 'Basic ' + token}
r = requests.get(url, headers=header)
data = r.json()
#1-Negligible, 2-Unknown, 3-Low, 4-Medium, 5-High
vulnerabilities = [[],[],[],[],[]]

for vulnerability in data:
        vulnerabilities[vulnerability['severity']-1].append(vulnerability)

url = "https://"+registry_url+"/api/projects?name="+repository_name
r = requests.get(url, headers=header)
data_project = r.json()
project_id = str(data_project[0]['project_id'])
image_link = "https://"+registry_url+"/harbor/projects/"+project_id+"/repositories/"+repository_name+"%2F"+image+"/tags/"+tag

print("Negligible : ", len(vulnerabilities[0]))
print("Unknown : ", len(vulnerabilities[1]))
print("Low : ", len(vulnerabilities[2]))
print("Medium : ", len(vulnerabilities[3]))
print("High : ", len(vulnerabilities[4]))

print("For more informations about the vulnerabilities, please check at : "+image_link)

