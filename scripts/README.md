## scripts folder

### This folder is a helper that can genrate project template, etc.
### So do not use it at your project just including ox

### subproject_template.py

This script is used to generate a new subproject template.

#### Example: Create a subproject
$ cd ~/ox

$ python scripts/subproject_template.py myproject -p myproject/ -d "description of it"

### Create remote package
$ xmake package -f remote -P ./myproject -o remote

$ rm -rf ./myproject/remote/packages/t (if your project starts with 't', then run rm -rf ./myproject/remote/packages/t/test)