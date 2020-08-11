



python setup.py sdist upload -r sneak

your local ~/.pypirc needs to contain
```
[distutils]
index-servers =
  sneak
[sneak]
repository: http://pypi.sneakycorp.htb:8080/
username: pypi
password: soufianeelhaoui
```

/home/low/.ssh needs to exist on your local machine...
