# Boilerplate-FlaskRestMongoTornado
A Python Boilerplate Project for flask, mongoengine, flask_mongoengine, flask-restful, tornado and Flask-Script

## Getting Started
To get you started you can simply clone the Boilerplate-FlaskRestMongoTornado repository and install the dependencies:

### Clone Boilerplate-FlaskRestMongoTornado
```python
git clone https://github.com/zerodine/Boilerplate-FlaskRestMongoTornado.git
cd Boilerplate-FlaskRestMongoTornado
```

### Install Dependencies
We have some dependencies in this project. Just use pip:
```python
pip install flask
pip install mongoengine
pip install flask_mongoengine
pip install flask-restful
pip install tornado
pip install Flask-Script
```

## Directory Layout

    flaskdemo/                  --> demo project, just rename or copy it
      
      apps/                     --> all the apps go in here
        core/                   --> demo app called core
          commands/             --> cli commands (flask-script)
            demo.py             --> just a demo command
          config/               --> config files for app
            config.py           --> general config for the app (environment does not matter here)
            config_dev.py       --> config for dev environment
            config_test.py      --> config for test environment
            config_prod.py      --> config for test environment
          resources/            --> app resources 
            demo.py             --> a demo resource with a simply get method
          views/                --> app views
            demo.py             --> a demo which returns a simple string
       
      config/                   --> config files for project
        config.py               --> general config for the project (environment does not matter here)
        config_dev.py           --> config for dev environment
        config_test.py          --> config for test environment
        config_prod.py          --> config for test environment

      manage.py                 --> manage (e.g. import commands)
      runserver.py              --> run script
      
## Commands

### Create command

To create a new command simply make a file in project/apps/app-name/commands with the command in it. Here is a example:

```python
from flask.ext.script import Command

class Demo(Command):
    """
        prints hello world
    """

    def run(self):
        print "hello world"
```

### Add command to project

To add the command to the project, add following line to manage.py

```python
from flaskdemo.apps.core.commands import sub_manager as core_sub_manager
manager.add_command("core", core_sub_manager)
```

## Contact
For more information about this project, checkout:
  * http://zerodine.com
  * http://flask.pocoo.org
  * http://flask-restful.readthedocs.org/en/latest/