0x03. AirBnB clone - Deploy static
DevOps
Python
SysAdmin
Scripting
CI/CD
 By: Guillaume, CTO at Holberton School
 Weight: 1
 Project will start Mar 6, 2024 6:00 AM, must end by Mar 8, 2024 6:00 AM
 Checker was released at Mar 6, 2024 6:00 PM
 An auto review will be launched at the deadline
Concepts
For this project, we expect you to look at these concepts:

[CI/CD](https://digital.ai/catalyst-blog/walk-before-you-run-understanding-ci-in-cd/)
The lean/agile methodology (See:[ Twelve Principles of Agile Software](https://agilemanifesto.org/principles.html)) is now widely used by the industry and one of its key principles is to iterate as fast as possible. If you apply this to software engineering, it means that you should:

code
ship your code
measure the impact
learn from it
fix or improve it
start over
As fast as possible and with small iterations in days or even hours (whereas it used to be weeks or even months). One big advantage is that if product development is going the wrong direction, fast iteration will allow to quickly detect this, and avoid wasting time.

From a technical point of view, quicker iterations mean fewer lines of code being pushed at every deploy, which allows easy performance impact measurement and easy troubleshooting if something goes wrong (better to debug a small code change than weeks of new code).



Applied to software engineering, CI/CD (Continuous Integration/Continuous Deployment) is a principle that allows individuals or teams to have a lean/agile way of working.

This translates to a “shipping pipeline” which is often built with multiple tools such as:

Shipping the code:
Capistrano, Fabric
Encapsulating the code
Docker, Packer
Testing the code
Jenkins, CircleCi, Travis
Measuring the code
Datadog, Newrelic, Wavefront
[AirBnB clone]()
AirBnB clone


I know you were waiting for it: it’s here!

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the [AirBnB website.](https://www.airbnb.com/)

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
A website (the front-end) that shows the final product to everybody: static and dynamic
A database or files that store data (data = objects)
An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
Final product
 

Concepts to learn
Unittest - and please work all together on tests cases
Python packages concept page
Serialization/Deserialization
*args, **kwargs
datetime
More coming soon!
Steps
You won’t build this application all at once, but step by step.

Each step will link to a concept:

The console
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine



Web static
learn HTML/CSS
create the HTML of your application
create template of each object


MySQL storage
replace the file storage by a Database storage
map your models to a table in database by using an O.R.M.


Web framework - templating
create your first web server in Python
make your static HTML file dynamic by using objects stored in a file or database


RESTful API
expose all your objects stored via a JSON web interface
manipulate your objects via a RESTful API


Web dynamic
learn JQuery
load objects from the client side by using your own RESTful API


Files and Directories
models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
tests directory will contain all unit tests.
console.py file is the entry point of our command interpreter.
models/base_model.py file is the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.
Storage
Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:

Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
Provide default value of any attribute
In the future, provide the same model behavior for file storage or database storage
How can I store my instances?
That’s a good question. So let’s take a look at this code:

class Student():
    def __init__(self, name):
        self.name = name

students = []
s = Student("John")
students.append(s)
Here, I’m creating a student and store it in a list. But after this program execution, my Student instance doesn’t exist anymore.

class Student():
    def __init__(self, name):
        self.name = name

students = reload() # recreate the list of Student objects from a file
s = Student("John")
students.append(s)
save(students) # save all Student objects to a file
Nice!

But how it works?

First, let’s look at save(students):

Can I write each Student object to a file => NO, it will be the memory representation of the object. For another program execution, this memory representation can’t be reloaded.
Can I write each Student.name to a file => YES, but imagine you have other attributes to describe Student? It would start to be become too complex.
The best solution is to convert this list of Student objects to a JSON representation.

Why JSON? Because it’s a standard representation of object. It allows us to share this data with other developers, be human readable, but mainly to be understood by another language/program.

Example:

My Python program creates Student objects and saves them to a JSON file
Another Javascript program can read this JSON file and manipulate its own Student class/representation
And the reload()? now you know the file is a JSON file representing all Student objects. So reload() has to read the file, parse the JSON string, and re-create Student objects based on this data-structure.

File storage == JSON serialization
For this first step, you have to write in a file all your objects/instances created/updated in your command interpreter and restore them when you start it. You can’t store and restore a Python instance of a class as “Bytes”, the only way is to convert it to a serializable data structure:

convert an instance to Python built in serializable data structure (list, dict, number and string) - for us it will be the method my_instance.to_json() to retrieve a dictionary
convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us it will be a my_string = JSON.dumps(my_dict)
write this string to a file on disk
And the process of deserialization?

The same but in the other way:

read a string from a file on disk
convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us it will be a my_dict = JSON.loads(my_string)
convert this data structure to instance - for us it will be a my_instance = MyObject(my_dict)
*args, **kwargs
[How To Use them](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)

How do you pass arguments to a function?

def my_fct(param_1, param_2):
    ...

my_fct("Best", "School")
But with this function definition, you must call my_fct with 2 parameters, no more, no less.

Can it be dynamic? Yes you can:

def my_fct(*args, **kwargs):
    ...

my_fct("Best", "School")
What? What’s *args and **kwargs?

*args is a Tuple that contains all arguments
*kwargs is a dictionary that contains all arguments by key/value
A dictionary? But why?

So, to make it clear, *args is the list of anonymous arguments, no name, just an order. **kwargs is the dictionary with all named arguments.

Examples:

def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

my_fct() # () - {}
my_fct("Best") # ('Best',) - {}
my_fct("Best", 89) # ('Best', 89) - {}
my_fct(name="Best") # () - {'name': 'Best'}
my_fct(name="Best", number=89) # () - {'name': 'Best', 'number': 89}
my_fct("School", 12, name="Best", number=89) # ('School', 12) - {'name': 'Best', 'number': 89}
Perfect? Of course you can mix both, but the order should be first all anonymous arguments, and after named arguments.

Last example:

def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

a_dict = { 'name': "Best", 'age': 89 }

my_fct(a_dict) # ({'age': 89, 'name': 'Best'},) - {}
my_fct(*a_dict) # ('age', 'name') - {}
my_fct(**a_dict) # () - {'age': 89, 'name': 'Best'}
You can play with these 2 arguments to clearly understand where and how your variables are stored.

datetime
datetime is a Python module to manipulate date, time etc…

In this example, you create an instance of datetime with the current date and time:

from datetime import datetime

date_now = datetime.now()
print(type(date_now)) # <class 'datetime.datetime'>
print(date_now) # 2017-06-08 20:42:42.170922
date_now is an object, so you can manipulate it:

from datetime import timedelta

date_tomorrow = date_now + timedelta(days=1)
print(date_tomorrow) # 2017-06-09 20:42:42.170922
… you can also store it:

a_dict = { 'my_date': date_now }
print(type(a_dict['my_date'])) # <class 'datetime.datetime'>
print(a_dict) # {'my_date': datetime.datetime(2017, 6, 8, 20, 42, 42, 170922)}
What? What’s this format when a datetime instance is in a datastructure??? It’s unreadable.

How to make it readable: [strftime](https://strftime.org/)

print(date_now.strftime("%A")) # Thursday
print(date_now.strftime("%A %d %B %Y at %H:%M:%S")) # Thursday 08 June 2017 at 20:42:42

Background Context
Ever since you completed project 0x0F. Load balancer of the SysAdmin track, you’ve had 2 web servers + 1 load balancer but nothing to distribute with them.

It’s time to make your work public!

In this first deployment project, you will be deploying your web_static work. You will use Fabric (for Python3). Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution. This concept is important: execute commands locally or remotely. Locally means in your laptop (physical laptop or inside your Vagrant), and Remotely means on your server(s). Fabric is taking care of all network connections (SSH, SCP etc.), it’s an easy tool for transferring, executing, etc. commands from locale to a remote server.

Before starting, please fork the repository AirBnB_clone_v2 from your partner if you don’t have it



Resources
Read or watch:

[How to use Fabric](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments)
[How to use Fabric in Python](https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python)
[Fabric and command line options](https://docs.fabfile.org/en/1.13/usage/fab.html)
[CI/CD concept page](https://intranet.alxswe.com/concepts/43)
[Nginx configuration for beginners](https://nginx.org/en/docs/beginners_guide.html)
[Difference between root and alias on NGINX](https://blog.heitorsilva.com/en/nginx/diferenca-entre-root-e-alias-do-nginx/)
[Fabric for Python 3](https://github.com/mathiasertl/fabric)
[Fabric Documentation](https://www.fabfile.org/)
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is Fabric
How to deploy code to a server easily
What is a tgz archive
How to execute Fabric command locally
How to execute Fabric command remotely
How to transfer files with Fabric
How to manage Nginx configuration
What is the difference between root and alias in a Nginx configuration
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.0)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the folder of the project is mandatory
Your code should use the PEP 8 style (version 1.7.*)
Your Fabric file must work with Fabric 3 version 1.14.post1 (installation instruction below)
All your files must be executable
The length of your files will be tested using wc
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Bash Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file at the root of the folder of the project is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu20.04.1 via apt-get) without any errors
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
More Info
Install Fabric for Python 3 - version 1.14.post1
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install build-essential
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install setuptools==40.1.0
$ pip3 install cryptography==2.8
$ pip3 install bcrypt==3.1.7
$ pip3 install PyNaCl==1.3.0
$ pip3 install Fabric3==1.14.post1
Video library(1 total)
Search by title
Deploy static files with Fabric
Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Prepare your web servers
mandatory
Write a Bash script that sets up your web servers for the deployment of web_static. It must:

Install Nginx if it not already installed
Create the folder /data/ if it doesn’t already exist
Create the folder /data/web_static/ if it doesn’t already exist
Create the folder /data/web_static/releases/ if it doesn’t already exist
Create the folder /data/web_static/shared/ if it doesn’t already exist
Create the folder /data/web_static/releases/test/ if it doesn’t already exist
Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
Use alias inside your Nginx configuration
[Tip](https://stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)
Your program should always exit successfully. Don’t forget to run your script on both of your web servers.

In optional, you will redo this task but by using Puppet

ubuntu@89-web-01:~/$ sudo ./0-setup_web_static.sh
ubuntu@89-web-01:~/$ echo $?
0
ubuntu@89-web-01:~/$ ls -l /data
total 4
drwxr-xr-x 1 ubuntu ubuntu     4096 Mar  7 05:17 web_static
ubuntu@89-web-01:~/$ ls -l /data/web_static
total 8
lrwxrwxrwx 1 ubuntu ubuntu   30 Mar 7 22:30 current -> /data/web_static/releases/test
drwxr-xr-x 3 ubuntu ubuntu 4096 Mar 7 22:29 releases
drwxr-xr-x 2 ubuntu ubuntu 4096 Mar 7 22:29 shared
ubuntu@89-web-01:~/$ ls /data/web_static/current
index.html
ubuntu@89-web-01:~/$ cat /data/web_static/current/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: 0-setup_web_static.sh
   
1. Compress before sending
mandatory
Write a Fabric script that generates a [.tgz](https://en.wikipedia.org/wiki/Tar_%28computing%29) archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.

Prototype: def do_pack():
All files in the folder web_static must be added to the final archive
All archives must be stored in the folder versions (your function should create this folder if it doesn’t exist)
The name of the archive created must be web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if the archive has been correctly generated. Otherwise, it should return None
guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 1-pack_web_static.py do_pack 
Packing web_static to versions/web_static_20170314233357.tgz
[localhost] local: tar -cvzf versions/web_static_20170314233357.tgz web_static
web_static/
web_static/.DS_Store
web_static/0-index.html
web_static/1-index.html
web_static/100-index.html
web_static/2-index.html
web_static/3-index.html
web_static/4-index.html
web_static/5-index.html
web_static/6-index.html
web_static/7-index.html
web_static/8-index.html
web_static/images/
web_static/images/icon.png
web_static/images/icon_bath.png
web_static/images/icon_bed.png
web_static/images/icon_group.png
web_static/images/icon_pets.png
web_static/images/icon_tv.png
web_static/images/icon_wifi.png
web_static/images/logo.png
web_static/index.html
web_static/styles/
web_static/styles/100-places.css
web_static/styles/2-common.css
web_static/styles/2-footer.css
web_static/styles/2-header.css
web_static/styles/3-common.css
web_static/styles/3-footer.css
web_static/styles/3-header.css
web_static/styles/4-common.css
web_static/styles/4-filters.css
web_static/styles/5-filters.css
web_static/styles/6-filters.css
web_static/styles/7-places.css
web_static/styles/8-places.css
web_static/styles/common.css
web_static/styles/filters.css
web_static/styles/footer.css
web_static/styles/header.css
web_static/styles/places.css
web_static packed: versions/web_static_20170314233357.tgz -> 21283Bytes

Done.
guillaume@ubuntu:~/AirBnB_clone_v2$ ls -l versions/web_static_20170314233357.tgz
-rw-rw-r-- 1 guillaume guillaume 21283 Mar 14 23:33 versions/web_static_20170314233357.tgz
guillaume@ubuntu:~/AirBnB_clone_v2$
Repo:

GitHub repository: AirBnB_clone_v2
File: 1-pack_web_static.py
   
2. Deploy archive!
mandatory
Write a Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to your web servers, using the function do_deploy:

Prototype: def do_deploy(archive_path):
Returns False if the file at the path archive_path doesn’t exist
The script should take the following steps:
Upload the archive to the /tmp/ directory of the web server
Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
Delete the archive from the web server
Delete the symbolic link /data/web_static/current from the web server
Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
All remote commands must be executed on your both web servers (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
Returns True if all operations have been done correctly, otherwise returns False
You must use this script to deploy it on your servers: xx-web-01 and xx-web-02
In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =...)

Disclaimer: commands execute by Fabric displayed below are linked to the way we implemented the archive function do_pack - like the mv command - depending of your implementation of it, you may don’t need it

guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20170315003959.tgz -i my_ssh_private_key -u ubuntu
[52.55.249.213] Executing task 'do_deploy'
[52.55.249.213] put: versions/web_static_20170315003959.tgz -> /tmp/web_static_20170315003959.tgz
[52.55.249.213] run: mkdir -p /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: rm /tmp/web_static_20170315003959.tgz
[52.55.249.213] run: mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/
[52.55.249.213] run: rm -rf /data/web_static/releases/web_static_20170315003959/web_static
[52.55.249.213] run: rm -rf /data/web_static/current
[52.55.249.213] run: ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current
New version deployed!
[54.157.32.137] Executing task 'deploy'
[54.157.32.137] put: versions/web_static_20170315003959.tgz -> /tmp/web_static_20170315003959.tgz
[54.157.32.137] run: mkdir -p /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: tar -xzf /tmp/web_static_20170315003959.tgz -C /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: rm /tmp/web_static_20170315003959.tgz
[54.157.32.137] run: mv /data/web_static/releases/web_static_20170315003959/web_static/* /data/web_static/releases/web_static_20170315003959/
[54.157.32.137] run: rm -rf /data/web_static/releases/web_static_20170315003959/web_static
[54.157.32.137] run: rm -rf /data/web_static/current
[54.157.32.137] run: ln -s /data/web_static/releases/web_static_20170315003959/ /data/web_static/current
New version deployed!

Done.
Disconnecting from 54.157.32.137... done.
Disconnecting from 52.55.249.213... done.
guillaume@ubuntu:~/AirBnB_clone_v2$ 
guillaume@ubuntu:~/AirBnB_clone_v2$ curl 54.157.32.137/hbnb_static/0-index.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>AirBnB clone</title>
    </head>
    <body style="margin: 0px; padding: 0px;">
        <header style="height: 70px; width: 100%; background-color: #FF0000">
        </header>

        <footer style="position: absolute; left: 0; bottom: 0; height: 60px; width: 100%; background-color: #00FF00; text-align: center; overflow: hidden;">
            <p style="line-height: 60px; margin: 0px;">Holberton School</p>
        </footer>
    </body>
</html>
guillaume@ubuntu:~/AirBnB_clone_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: 2-do_deploy_web_static.py
   
3. Full deployment
mandatory
Write a Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy:

Prototype: def deploy():
The script should take the following steps:
Call the do_pack() function and store the path of the created archive
Return False if no archive has been created
Call the do_deploy(archive_path) function, using the new path of the new archive
Return the return value of do_deploy
All remote commands must be executed on both of web your servers (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
You must use this script to deploy it on your servers: xx-web-01 and xx-web-02
In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)

guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
[52.55.249.213] Executing task 'deploy'
Packing web_static to versions/web_static_20170315015620.tgz
[localhost] local: tar -cvzf versions/web_static_20170315015620.tgz web_static
web_static/
web_static/0-index.html
web_static/1-index.html
web_static/100-index.html
web_static/2-index.html
web_static/3-index.html
web_static/4-index.html
web_static/5-index.html
web_static/6-index.html
web_static/7-index.html
web_static/8-index.html
web_static/images/
web_static/images/icon.png
web_static/images/icon_bath.png
web_static/images/icon_bed.png
web_static/images/icon_group.png
web_static/images/icon_pets.png
web_static/images/icon_tv.png
web_static/images/icon_wifi.png
web_static/images/logo.png
web_static/index.html
web_static/styles/
web_static/styles/100-places.css
web_static/styles/2-common.css
web_static/styles/2-footer.css
web_static/styles/2-header.css
web_static/styles/3-common.css
web_static/styles/3-footer.css
web_static/styles/3-header.css
web_static/styles/4-common.css
web_static/styles/4-filters.css
web_static/styles/5-filters.css
web_static/styles/6-filters.css
web_static/styles/7-places.css
web_static/styles/8-places.css
web_static/styles/common.css
web_static/styles/filters.css
web_static/styles/footer.css
web_static/styles/header.css
web_static/styles/places.css
web_static packed: versions/web_static_20170315015620.tgz -> 27280335Bytes
[52.55.249.213] put: versions/web_static_20170315015620.tgz -> /tmp/web_static_20170315015620.tgz
[52.55.249.213] run: mkdir -p /data/web_static/releases/web_static_20170315015620/
[52.55.249.213] run: tar -xzf /tmp/web_static_20170315015620.tgz -C /data/web_static/releases/web_static_20170315015620/
[52.55.249.213] run: rm /tmp/web_static_20170315015620.tgz
[52.55.249.213] run: mv /data/web_static/releases/web_static_20170315015620/web_static/* /data/web_static/releases/web_static_20170315015620/
[52.55.249.213] run: rm -rf /data/web_static/releases/web_static_20170315015620/web_static
[52.55.249.213] run: rm -rf /data/web_static/current
[52.55.249.213] run: ln -s /data/web_static/releases/web_static_20170315015620/ /data/web_static/current
New version deployed!
[54.157.32.137] Executing task 'deploy'
[54.157.32.137] put: versions/web_static_20170315015620.tgz -> /tmp/web_static_20170315015620.tgz
[54.157.32.137] run: mkdir -p /data/web_static/releases/web_static_20170315015620/
[54.157.32.137] run: tar -xzf /tmp/web_static_20170315015620.tgz -C /data/web_static/releases/web_static_20170315015620/
[54.157.32.137] run: rm /tmp/web_static_20170315015620.tgz
[54.157.32.137] run: mv /data/web_static/releases/web_static_20170315015620/web_static/* /data/web_static/releases/web_static_20170315015620/
[54.157.32.137] run: rm -rf /data/web_static/releases/web_static_20170315015620/web_static
[54.157.32.137] run: rm -rf /data/web_static/current
[54.157.32.137] run: ln -s /data/web_static/releases/web_static_20170315015620/ /data/web_static/current
New version deployed!

Done.
Disconnecting from 54.157.32.137... done.
Disconnecting from 52.55.249.213... done.
guillaume@ubuntu:~/AirBnB_clone_v2$ 
guillaume@ubuntu:~/AirBnB_clone_v2$ curl 54.157.32.137/hbnb_static/0-index.html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>AirBnB clone</title>
    </head>
    <body style="margin: 0px; padding: 0px;">
        <header style="height: 70px; width: 100%; background-color: #FF0000">
        </header>

        <footer style="position: absolute; left: 0; bottom: 0; height: 60px; width: 100%; background-color: #00FF00; text-align: center; overflow: hidden;">
            <p style="line-height: 60px; margin: 0px;">Holberton School</p>
        </footer>
    </body>
</html>
guillaume@ubuntu:~/AirBnB_clone_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: 3-deploy_web_static.py
   
4. Keep it clean!
#advanced
Write a Fabric script (based on the file 3-deploy_web_static.py) that deletes out-of-date archives, using the function do_clean:

Prototype: def do_clean(number=0):
number is the number of the archives, including the most recent, to keep.
If number is 0 or 1, keep only the most recent version of your archive.
if number is 2, keep the most recent, and second most recent versions of your archive.
etc.
Your script should:
Delete all unnecessary archives (all archives minus the number to keep) in the versions folder
Delete all unnecessary archives (all archives minus the number to keep) in the /data/web_static/releases folder of both of your web servers
All remote commands must be executed on both of your web servers (using the env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
In the following example, the SSH key and the username used for accessing to the server are passed in the command line. Of course, you could define them as Fabric environment variables (ex: env.user =…)

guillaume@ubuntu:~/AirBnB_clone_v2$ ls -ltr versions
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015414.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015448.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015507.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015620.tgz
guillaume@ubuntu:~/AirBnB_clone_v2$ fab -f 100-clean_web_static.py do_clean:number=2 -i my_ssh_private_key -u ubuntu > /dev/null 2>&1
guillaume@ubuntu:~/AirBnB_clone_v2$ ls -ltr versions
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015507.tgz
-rw-r--r-- 1 vagrant vagrant 27280335 Mar 15  2017 web_static_20170315015620.tgz
guillaume@ubuntu:~/AirBnB_clone_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: 100-clean_web_static.py
   
5. Puppet for setup
#advanced
Redo the task #0 but by using Puppet:

ubuntu@89-web-01:~/$ puppet apply 101-setup_web_static.pp
....
ubuntu@89-web-01:~/$ ls -l /data
total 4
drwxr-xr-x 1 ubuntu ubuntu     4096 Mar  7 05:17 web_static
ubuntu@89-web-01:~/$ ls -l /data/web_static
total 8
lrwxrwxrwx 1 root root   30 Mar 7 22:30 current -> /data/web_static/releases/test
drwxr-xr-x 3 root root 4096 Mar 7 22:29 releases
drwxr-xr-x 2 root root 4096 Mar 7 22:29 shared
ubuntu@89-web-01:~/$ ls /data/web_static/current
index.html
ubuntu@89-web-01:~/$ cat /data/web_static/current/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: 101-setup_web_static.pp






Environment variables will be your best friend for this project!

HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
HBNB_MYSQL_USER: the username of your MySQL
HBNB_MYSQL_PWD: the password of your MySQL
HBNB_MYSQL_HOST: the hostname of your MySQL
HBNB_MYSQL_DB: the database name of your MySQL
HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)
Resources
Read or watch:

[cmd module](https://docs.python.org/3/library/cmd.html)
[packages concept page]
[unittest module](https://docs.python.org/3/library/unittest.html#module-unittest)
[args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
[SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
[How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
[Python3 and environment variables](https://docs.python.org/3/library/os.html#os.getenv)
[SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
[MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is Unit testing and how to implement it in a large project
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function
How to create a MySQL database
How to create a MySQL user and grant it privileges
What ORM means
How to map a Python Class to a MySQL table
How to handle 2 different storage engines with the same codebase
How to use environment variables
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Python Unit Tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project: ex: for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
We strongly encourage you to work together on test cases, so that you don’t miss any edge cases
SQL Scripts
Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0
Your files will be executed with SQLAlchemy version 1.4.x
All your files should end with a new line
All your SQL queries should have a comment just before (i.e. syntax above)
All your files should start by a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE…)
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc
GitHub
There should be one project repository per group. If you clone/fork/whatever a partner’s project repository with the same name before the second deadline, you risk a 0% score.

More Info


Comments for your SQL file:
$ cat my_script.sql
-- first 3 students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
Video library(2 total)
Search by title
HBNB - storage abstraction
AirBnB console
Tasks
0. Fork me if you can!
mandatory
In the industry, you will work on an existing codebase 90% of the time. Your first thoughts upon looking at it might include:

“Who did this code?”
“How it works?”
“Where are unittests?”
“Where is this?”
“Why did they do that like this?”
“I don’t understand anything.”
“… I will refactor everything…”
But the worst thing you could possibly do is to redo everything. Please don’t do that! Note: the existing codebase might be perfect, or it might have errors. Don’t always trust the existing codebase!

For this project you will fork this codebase:

update the repository name to AirBnB_clone_v2
update the README.md with your information but don’t delete the initial authors
If you are the owner of this repository, please create a new repository named AirBnB_clone_v2 with the same content of AirBnB_clone

Repo:

GitHub repository: AirBnB_clone_v2
   
1. Bug free!
mandatory
Do you remember the unittest module?

This codebase contains many test cases. Some are missing, but the ones included cover the basic functionality of the program.

guillaume@ubuntu:~/AirBnB_v2$ python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$ 
All your unittests must pass without any errors at anytime in this project, with each storage engine!. Same for PEP8!

guillaume@ubuntu:~/AirBnB_v2$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$ 
Some tests won’t be relevant for some type of storage, please skip them by using the skipIf feature of [the Unittest module - 26.3.6. Skipping tests and expected failures.](https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures) Of course, the number of tests must be higher than the current number of tests, so if you decide to skip a test, you should write a new test!

How to test with MySQL?
First, you create a specific database for it (next tasks). After, you have to remember what the purpose of an unittest?

“Assert a current state (objects/data/database), do an action, and validate this action changed (or not) the state of your objects/data/database”

For example, “you want to validate that the create State name="California" command in the console will add a new record in your table states in your database”, here steps for your unittest:

get the number of current records in the table states (my using a MySQLdb for example - but not SQLAlchemy (remember, you want to test if it works, so it’s better to isolate from the system))
execute the console command
get (again) the number of current records in the table states (same method, with MySQLdb)
if the difference is +1 => test passed
Repo:

GitHub repository: AirBnB_clone_v2
  
2. Console improvements
mandatory
Update the def do_create(self, arg): function of your command interpreter (console.py) to allow for object creation with given parameters:

Command syntax: create <Class name> <param 1> <param 2> <param 3>...
Param syntax: <key name>=<value>
Value syntax:
String: "<value>" => starts with a double quote
any double quote inside the value must be escaped with a backslash \
all underscores _ must be replace by spaces . Example: You want to set the string My little house to the attribute name, your command line must be name="My_little_house"
Float: <unit>.<decimal> => contains a dot .
Integer: <number> => default case
If any parameter doesn’t fit with these requirements or can’t be recognized correctly by your program, it must be skipped
Don’t forget to add tests for this new feature!

Also, this new feature will be tested here only with FileStorage engine.

guillaume@ubuntu:~/AirBnB_v2$ cat test_params_create
create State name="California"
create State name="Arizona"
all State

create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297
all Place
guillaume@ubuntu:~/AirBnB_v2$ cat test_params_create | ./console.py 
(hbnb) d80e0344-63eb-434a-b1e0-07783522124e
(hbnb) 092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7
(hbnb) [[State] (d80e0344-63eb-434a-b1e0-07783522124e) {'id': 'd80e0344-63eb-434a-b1e0-07783522124e', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842160), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842235), 'name': 'California'}, [State] (092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7) {'id': '092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842779), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842792), 'name': 'Arizona'}]
(hbnb) (hbnb) 76b65327-9e94-4632-b688-aaa22ab8a124
(hbnb) [[Place] (76b65327-9e94-4632-b688-aaa22ab8a124) {'number_bathrooms': 2, 'longitude': -122.431297, 'city_id': '0001', 'user_id': '0001', 'latitude': 37.773972, 'price_by_night': 300, 'name': 'My little house', 'id': '76b65327-9e94-4632-b688-aaa22ab8a124', 'max_guest': 10, 'number_rooms': 4, 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843774), 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843747)}]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$
Repo:

GitHub repository: AirBnB_clone_v2
File: console.py, models/, tests/
   
3. MySQL setup development
mandatory
Write a script that prepares a MySQL server for the project:

A database hbnb_dev_db
A new user hbnb_dev (in localhost)
The password of hbnb_dev should be set to hbnb_dev_pwd
hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail
guillaume@ubuntu:~/AirBnB_v2$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db
Enter password: 
hbnb_dev_db
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p
Enter password: 
Grants for hbnb_dev@localhost
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost'
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: setup_mysql_dev.sql
   
4. MySQL setup test
mandatory
Write a script that prepares a MySQL server for the project:

A database hbnb_test_db
A new user hbnb_test (in localhost)
The password of hbnb_test should be set to hbnb_test_pwd
hbnb_test should have all privileges on the database hbnb_test_db (and only this database)
hbnb_test should have SELECT privilege on the database performance_schema (and only this database)
If the database hbnb_test_db or the user hbnb_test already exists, your script should not fail
guillaume@ubuntu:~/AirBnB_v2$ cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
Enter password: 
hbnb_test_db
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
Enter password: 
Grants for hbnb_test@localhost
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost'
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: setup_mysql_test.sql
   
5. Delete object
mandatory
Update FileStorage: (models/engine/file_storage.py)

Add a new public instance method: def delete(self, obj=None): to delete obj from __objects if it’s inside - if obj is equal to None, the method should not do anything
Update the prototype of def all(self) to def all(self, cls=None) - that returns the list of objects of one type of class. Example below with State - it’s an optional filtering
guillaume@ubuntu:~/AirBnB_v2$ cat main_delete.py
#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])        

# Delete the new State
fs.delete(new_state)

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

guillaume@ubuntu:~/AirBnB_v2$ ./main_delete.py
All States: 0
New State: [State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
All States: 1
[State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
Another State: [State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
All States: 2
[State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
[State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
All States: 1
[State] (37705d25-8903-4318-9303-6d6d336a22c1) {'name': 'Nevada', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 34, 619133), 'id': '37705d25-8903-4318-9303-6d6d336a22c1'}
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: models/engine/file_storage.py
   
6. DBStorage - States and Cities
mandatory
SQLAlchemy will be your best friend!

It’s time to change your storage engine and use SQLAlchemy



In the following steps, you will make multiple changes:

the biggest one is the transition between FileStorage and DBStorage: In the industry, you will never find a system who can work with both in the same time - but you will find a lot of services who can manage multiple storage systems. (for example, logs service: in memory, in disk, in database, in ElasticSearch etc…) - The main concept behind is the abstraction: Make your code running without knowing how it’s stored.
add attributes for SQLAlchemy: they will be class attributes, like previously, with a “weird” value. Don’t worry, these values are for description and mapping to the database. If you change one of these values, or add/remove one attribute of the a model, you will have to delete the database and recreate it in SQL. (Yes it’s not optimal, but for development purposes, it’s ok. In production, we will add “migration mechanism” - for the moment, don’t spend time on it.)
Please follow all these steps:

Update BaseModel: (models/base_model.py)

Create Base = declarative_base() before the class definition of BaseModel
Note! BaseModel does /not/ inherit from Base. All other classes will inherit from BaseModel to get common values (id, created_at, updated_at), where inheriting from Base will actually cause SQLAlchemy to attempt to map it to a table.
Add or replace in the class BaseModel:
class attribute id
represents a column containing a unique string (60 characters)
can’t be null
primary key
class attribute created_at
represents a column containing a datetime
can’t be null
default value is the current datetime (use datetime.utcnow())
class attribute updated_at
represents a column containing a datetime
can’t be null
default value is the current datetime (use datetime.utcnow())
Move the models.storage.new(self) from def __init__(self, *args, **kwargs): to def save(self): and call it just before models.storage.save()
In def __init__(self, *args, **kwargs):, manage kwargs to create instance attribute from this dictionary. Ex: kwargs={ 'name': "California" } => self.name = "California" if it’s not already the case
Update the to_dict() method of the class BaseModel:
remove the key _sa_instance_state from the dictionary returned by this method only if this key exists
Add a new public instance method: def delete(self): to delete the current instance from the storage (models.storage) by calling the method delete
Update City: (models/city.py)

City inherits from BaseModel and Base (respect the order)
Add or replace in the class City:
class attribute __tablename__ -
represents the table name, cities
class attribute name
represents a column containing a string (128 characters)
can’t be null
class attribute state_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to states.id
Update State: (models/state.py)

State inherits from BaseModel and Base (respect the order)
Add or replace in the class State:
class attribute __tablename__
represents the table name, states
class attribute name
represents a column containing a string (128 characters)
can’t be null
for DBStorage: class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state
for FileStorage: getter attribute cities that returns the list of City instances with state_id equals to the current State.id => It will be the FileStorage relationship between State and City
New engine DBStorage: (models/engine/db_storage.py)

Private class attributes:
__engine: set to None
__session: set to None
Public instance methods:
__init__(self):
create the engine (self.__engine)
the engine must be linked to the MySQL database and user created before (hbnb_dev and hbnb_dev_db):
dialect: mysql
driver: mysqldb
all of the following values must be retrieved via environment variables:
MySQL user: HBNB_MYSQL_USER
MySQL password: HBNB_MYSQL_PWD
MySQL host: HBNB_MYSQL_HOST (here = localhost)
MySQL database: HBNB_MYSQL_DB
don’t forget the option pool_pre_ping=True when you call create_engine
drop all tables if the environment variable HBNB_ENV is equal to test
all(self, cls=None):
query on the current database session (self.__session) all objects depending of the class name (argument cls)
if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
this method must return a dictionary: (like FileStorage)
key = <class-name>.<object-id>
value = object
new(self, obj): add the object to the current database session (self.__session)
save(self): commit all changes of the current database session (self.__session)
delete(self, obj=None): delete from the current database session obj if not None
reload(self):
create all tables in the database (feature of SQLAlchemy) (WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine))
create the current database session (self.__session) from the engine (self.__engine) by using a sessionmaker - the option expire_on_commit must be set to False ; and scoped_session - to make sure your Session is thread-safe
Update __init__.py: (models/__init__.py)

Add a conditional depending of the value of the environment variable HBNB_TYPE_STORAGE:
If equal to db:
Import DBStorage class in this file
Create an instance of DBStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)
Else:
Import FileStorage class in this file
Create an instance of FileStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)
This “switch” will allow you to change storage type directly by using an environment variable (example below)
State creation:

guillaume@ubuntu:~/AirBnB_v2$ echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 95a5abab-aa65-4861-9bc6-1da4a36069aa
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[State] (95a5abab-aa65-4861-9bc6-1da4a36069aa) {'name': 'California', 'id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'updated_at': datetime.datetime(2017, 11, 10, 0, 49, 54), 'created_at': datetime.datetime(2017, 11, 10, 0, 49, 54)}]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
created_at: 2017-11-10 00:49:54
updated_at: 2017-11-10 00:49:54
      name: California
guillaume@ubuntu:~/AirBnB_v2$ 
City creation:

guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) 4b457e66-c7c8-4f63-910f-fd91c3b7140b
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all City' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[City] (4b457e66-c7c8-4f63-910f-fd91c3b7140b) {'id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'updated_at': datetime.datetime(2017, 11, 10, 0, 52, 53), 'state_id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'name': 'San Francisco', 'created_at': datetime.datetime(2017, 11, 10, 0, 52, 53)]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Jose"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) a7db3cdc-30e0-4d80-ad8c-679fe45343ba
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
created_at: 2017-11-10 00:52:53
updated_at: 2017-11-10 00:52:53
      name: San Francisco
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
*************************** 2. row ***************************
        id: a7db3cdc-30e0-4d80-ad8c-679fe45343ba
created_at: 2017-11-10 00:53:19
updated_at: 2017-11-10 00:53:19
      name: San Jose
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: models/base_model.py, models/city.py, models/state.py, models/engine/db_storage.py, models/__init__.py
  
7. DBStorage - User
mandatory
Update User: (models/user.py)

User inherits from BaseModel and Base (respect the order)
Add or replace in the class User:
class attribute __tablename__
represents the table name, users
class attribute email
represents a column containing a string (128 characters)
can’t be null
class attribute password
represents a column containing a string (128 characters)
can’t be null
class attribute first_name
represents a column containing a string (128 characters)
can be null
class attribute last_name
represents a column containing a string (128 characters)
can be null
guillaume@ubuntu:~/AirBnB_v2$ echo 'create User email="gui@hbtn.io" password="guipwd" first_name="Guillaume" last_name="Snow"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$
guillaume@ubuntu:~/AirBnB_v2$ echo 'all User' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[User] (4f3f4b42-a4c3-4c20-a492-efff10d00c0b) {'updated_at': datetime.datetime(2017, 11, 10, 1, 17, 26), 'id': '4f3f4b42-a4c3-4c20-a492-efff10d00c0b', 'last_name': 'Snow', 'first_name': 'Guillaume', 'email': 'gui@hbtn.io', 'created_at': datetime.datetime(2017, 11, 10, 1, 17, 26), 'password': 'f4ce007d8e84e0910fbdd7a06fa1692d'}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM users\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
created_at: 2017-11-10 01:17:26
updated_at: 2017-11-10 01:17:26
     email: gui@hbtn.io
  password: guipwd
first_name: Guillaume
 last_name: Snow
guillaume@ubuntu:~/AirBnB_v2$
Repo:

GitHub repository: AirBnB_clone_v2
File: models/user.py
  
8. DBStorage - Place
mandatory
Update Place: (models/place.py)

Place inherits from BaseModel and Base (respect the order)
Add or replace in the class Place:
class attribute __tablename__
represents the table name, places
class attribute city_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to cities.id
class attribute user_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to users.id
class attribute name
represents a column containing a string (128 characters)
can’t be null
class attribute description
represents a column containing a string (1024 characters)
can be null
class attribute number_rooms
represents a column containing an integer
can’t be null
default value: 0
class attribute number_bathrooms
represents a column containing an integer
can’t be null
default value: 0
class attribute max_guest
represents a column containing an integer
can’t be null
default value: 0
class attribute price_by_night
represents a column containing an integer
can’t be null
default value: 0
class attribute latitude
represents a column containing a float
can be null
class attribute longitude
represents a column containing a float
can be null
Update User: (models/user.py)

Add or replace in the class User:
class attribute places must represent a relationship with the class Place. If the User object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his User should be named user
Update City: (models/city.py)

Add or replace in the class City:
class attribute places must represent a relationship with the class Place. If the City object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his City should be named cities
guillaume@ubuntu:~/AirBnB_v2$ echo 'create Place city_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b" user_id="4f3f4b42-a4c3-4c20-a492-efff10d00c0b" name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 longitude=-122.431297' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) ed72aa02-3286-4891-acbc-9d9fc80a1103
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all Place' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[Place] (ed72aa02-3286-4891-acbc-9d9fc80a1103) {'latitude': 37.774, 'city_id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'price_by_night': 120, 'id': 'ed72aa02-3286-4891-acbc-9d9fc80a1103', 'user_id': '4f3f4b42-a4c3-4c20-a492-efff10d00c0b', 'max_guest': 6, 'created_at': datetime.datetime(2017, 11, 10, 1, 22, 30), 'description': None, 'number_rooms': 3, 'longitude': -122.431, 'number_bathrooms': 1, 'name': '"Lovely place', 'updated_at': datetime.datetime(2017, 11, 10, 1, 22, 30)}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
              id: ed72aa02-3286-4891-acbc-9d9fc80a1103
      created_at: 2017-11-10 01:22:30
      updated_at: 2017-11-10 01:22:30
         city_id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
         user_id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
            name: "Lovely place"
     description: NULL
    number_rooms: 3
number_bathrooms: 1
       max_guest: 6
  price_by_night: 120
        latitude: 37.774
       longitude: -122.431
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: models/place.py, models/user.py, models/city.py
  
9. DBStorage - Review
mandatory
Update Review: (models/review.py)

Review inherits from BaseModel and Base (respect the order)
Add or replace in the class Review:
class attribute __tablename__
represents the table name, reviews
class attribute text
represents a column containing a string (1024 characters)
can’t be null
class attribute place_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to places.id
class attribute user_id
represents a column containing a string (60 characters)
can’t be null
is a foreign key to users.id
Update User: (models/user.py)

Add or replace in the class User:
class attribute reviews must represent a relationship with the class Review. If the User object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his User should be named user
Update Place: (models/place.py)

for DBStorage: class attribute reviews must represent a relationship with the class Review. If the Place object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his Place should be named place
for FileStorage: getter attribute reviews that returns the list of Review instances with place_id equals to the current Place.id => It will be the FileStorage relationship between Place and Review
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'create User email="bob@hbtn.io" password="bobpwd" first_name="Bob" last_name="Dylan"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) d93638d9-8233-4124-8f4e-17786592908b
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'create Review place_id="ed72aa02-3286-4891-acbc-9d9fc80a1103" user_id="d93638d9-8233-4124-8f4e-17786592908b" text="Amazing_place,_huge_kitchen"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) a2d163d3-1982-48ab-a06b-9dc71e68a791
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all Review' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[Review] (f2616ff2-f723-4d67-85dc-f050a38e0f2f) {'text': 'Amazing place, huge kitchen', 'place_id': 'ed72aa02-3286-4891-acbc-9d9fc80a1103', 'id': 'f2616ff2-f723-4d67-85dc-f050a38e0f2f', 'updated_at': datetime.datetime(2017, 11, 10, 4, 6, 25), 'created_at': datetime.datetime(2017, 11, 10, 4, 6, 25), 'user_id': 'd93638d9-8233-4124-8f4e-17786592908b'}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM reviews\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: f2616ff2-f723-4d67-85dc-f050a38e0f2f
created_at: 2017-11-10 04:06:25
updated_at: 2017-11-10 04:06:25
      text: Amazing place, huge kitchen
  place_id: ed72aa02-3286-4891-acbc-9d9fc80a1103
   user_id: d93638d9-8233-4124-8f4e-17786592908b
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: models/review.py, models/user.py, models/place.py
  
10. DBStorage - Amenity... and BOOM!
mandatory
Update Amenity: (models/amenity.py)

Amenity inherits from BaseModel and Base (respect the order)
Add or replace in the class Amenity:
class attribute __tablename__
represents the table name, amenities
class attribute name
represents a column containing a string (128 characters)
can’t be null
class attribute place_amenities must represent a relationship Many-To-Many between the class Place and Amenity. Please see below more detail: place_amenity in the Place update
Update Place: (models/place.py)

Add an instance of SQLAlchemy Table called place_amenity for creating the relationship Many-To-Many between Place and Amenity:
table name place_amenity
metadata = Base.metadata
2 columns:
place_id, a string of 60 characters foreign key of places.id, primary key in the table and never null
amenity_id, a string of 60 characters foreign key of amenities.id, primary key in the table and never null
Update Place class:
for DBStorage: class attribute amenities must represent a relationship with the class Amenity but also as secondary to place_amenity with option viewonly=False (place_amenity has been define previously)
for FileStorage:
Getter attribute amenities that returns the list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the Place
Setter attribute amenities that handles append method for adding an Amenity.id to the attribute amenity_ids. This method should accept only Amenity object, otherwise, do nothing.
What’s a Many-to-Many relationship?
In our system, we don’t want to duplicate amenities (for example, having 10000 time the amenity Wifi), so they will be unique. But, at least 2 places can have the same amenity (like Wifi for example). We are in the case of:

an amenity can be linked to multiple places
a place can have multiple amenities
= Many-To-Many

To make this link working, we will create a third table called place_amenity that will create these links.

And you are good, you have a new engine!

guillaume@ubuntu:~/AirBnB_v2$ cat main_place_amenities.py 
#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *

# creation of a State
state = State(name="California")
state.save()

# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./main_place_amenities.py
OK
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM amenities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 47321eb8-152a-46df-969a-440aa67a6d59
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Cable
*************************** 2. row ***************************
        id: 4a307e7f-68f9-438f-81c0-8325898dda2a
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Oven
*************************** 3. row ***************************
        id: b80aec52-d0c9-420a-8471-3254572954b6
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Wifi
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
              id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
      created_at: 2017-11-10 04:22:02
      updated_at: 2017-11-10 04:22:02
         city_id: 9d60df6e-31f7-430c-8162-69e89f4a17aa
         user_id: 9b37bd51-6aef-485f-bf10-c7ab83fea2e9
            name: House 1
     description: NULL
    number_rooms: 0
number_bathrooms: 0
       max_guest: 0
  price_by_night: 0
        latitude: NULL
       longitude: NULL
*************************** 2. row ***************************
              id: db549ae1-4500-4d0c-9b50-4b4978ed229e
      created_at: 2017-11-10 04:22:02
      updated_at: 2017-11-10 04:22:02
         city_id: 9d60df6e-31f7-430c-8162-69e89f4a17aa
         user_id: 9b37bd51-6aef-485f-bf10-c7ab83fea2e9
            name: House 2
     description: NULL
    number_rooms: 0
number_bathrooms: 0
       max_guest: 0
  price_by_night: 0
        latitude: NULL
       longitude: NULL
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM place_amenity\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
  place_id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
amenity_id: 47321eb8-152a-46df-969a-440aa67a6d59
*************************** 2. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: 47321eb8-152a-46df-969a-440aa67a6d59
*************************** 3. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: 4a307e7f-68f9-438f-81c0-8325898dda2a
*************************** 4. row ***************************
  place_id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
amenity_id: b80aec52-d0c9-420a-8471-3254572954b6
*************************** 5. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: b80aec52-d0c9-420a-8471-3254572954b6
guillaume@ubuntu:~/AirBnB_v2$ 
Repo:

GitHub repository: AirBnB_clone_v2
File: models/amenity.py, models/place.py















<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/justinmajetich/AirBnB_clone/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/user.py) [/models/place.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/place.py) [/models/city.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/city.py) [/models/amenity.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/amenity.py) [/models/state.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/state.py) [/models/review.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/justinmajetich/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>
