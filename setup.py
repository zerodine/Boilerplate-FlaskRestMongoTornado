from distutils.core import setup
import os

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["app/*", "runserver.py", "manage.py", "doc/*"]
buildNumber = os.environ.get('BUILD_NUMBER') if os.environ.get('BUILD_NUMBER') is not None else "9999"


setup(name = "cathedra",
    version = "0.0.1-%s" % buildNumber,
    description = "Cathedra Backend System",
    author = "zerodine",
    author_email = "info@zerodine.com",
    url = "zerodine.com",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['app'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'package' : files },
    #'runner' is in the root.
    scripts = ["runserver.py"],
    long_description = open('README.md', 'rt').read(),
    install_requires = ['flask', 'mongoengine', 'flask-mongoengine', 'flask-restful', 'tornado','Flask-Script', 'm2crypto', 'tornado']
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
)