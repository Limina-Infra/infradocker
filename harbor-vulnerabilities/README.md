# Harbor-vulnerabilities

Python scripts which will call the harbor api to get a recap of the vulnerabilities for the specified image or projects.

## How to use

To test it directly, run :
docker pull limina/harbor-vulnerabilities:latest

```docker
docker run limina/harbor-vulnerabilities:latest checkvulnerabilities.py <registry_url> <project_name> <image> <tag> <token> <optional: conditions>
# For conditions, the format is int,int,int,int
# Stand for Unknown, Low, Medium, High
# If you want only to put a condition for High vulnerability at 5, you will write the following : -1,-1,-1,5

ex : 
docker run limina/harbor-vulnerabilities:latest checkvulnerabilities.py my-registry.com myproject ubuntu 1.0 2fj29fj20843 -1,-1,10,3
```

```docker
docker run limina/harbor-vulnerabilities:latest checkallimages.py <registry_url> <projects> <token> <optional: conditions>
# For conditions, same as precedent
# For the projects, you can specify multiple projects : project1,project2,project3


ex : 
docker run limina/harbor-vulnerabilities:latest checkallimages.py my-registry.com project1,project2,project3 2fj29fj20843 -1,-1,10,3
```

Return a simple text 
```
Negligible : X
Unknown : X < Y
Low : X >= Y  BREACH OF CONDITION
Medium : X < Y
High : X >= Y  BREACH OF CONDITION
For more informations about the vulnerabilities, please check at : <link to the image>

And throw errors if breach of condition
```

