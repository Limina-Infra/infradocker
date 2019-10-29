# Harbor-vulnerabilities

A python script which will call the harbor api to get a recap of the vulnerabilities for the specified image.

## How to use

To test it directly, run :
docker pull limina/jenkins-slave
```docker
docker run limina/harbor-vulnerabilities <registry_url> <repository_name> <image> <tag> <token>
```

Return a simple text 
```
Negligible : X
Unknown : X
Low : X
Medium : X
High : X
For more informations about the vulnerabilities, please check at : <link to the image>
```

