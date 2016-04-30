Getting Started Todo's
- [x] add missing file requirements-dex.txt - its been renamed requirements/dev.txt
- [x] add note on when ElasticSeach apt-get package wouldnt load in both OS and ElasticSearch sections
- [x] fix django-nose spelling
- [x] look into redis-server package availabilty
        Found package has been added to the install instructions
- [x] fix multi row text make long lines
- [x] manage.py has excute bit set drop python
- [x] move up virtualenv activate
- [ ] show venvwrapper examples
- [x] add note on redis apt-get install strangeness with service errors
- [x] rearrange dependencies and install steps for proper flow
- [x] fix elasticsearch start do not run as root
- [x] move sudo apt-get update ... to start of lib section
- [x] add tcl8.5 to 3rd party section
- [X] remove django-nose requirement from doc add dev.txt fixed issue

# Getting Started
=================

These are some basic survival instructions to get a local instance of dailydot.com
installed and running. Some elbow grease will need to be put into making this easier
and more portable. However, with these directions and some luck, you'll be up and running!

If this is a clean and fresh build install please be sure to read the
[dependency section](#dependencies) to insure installation of all required software,
modules and libraries.


# Creating and Building Instance

if this is a new system build follow these [steps](#installing) to install the dependent
software. Once all dependant software has been installed ensure that to following software is
started and running.

[Redis Server](#redis)

[ElasticSearch](#elasticsearch)


## Database downloading and importing

### Switch to database user account
    
    sudo su - postgres

### Create database

    createdb dailydot -T template0 -E UTF8

### Login to  Heroku via Heroku-cli
    heroku login
 
### Get Database snapsot
    wget -O snapshot.dump `heroku pg:backups public-url -q --app dailydot`
    
### Load Data into Database
    
    pg_restore --verbose --clean --no-acl --no-owner -j 4 -d dailydot snapshot.dump

### Connect to the Daily Dot PostgreSQL database, change that user to superuser, and grant it all privileges on all Daily Dot tables

    psql dailydot
    alter user postgres superuser;
    grant all privileges on all tables in schema public to postgres;
    (quit psql)


## Cloning and Initializing Git Repository


    git clone https://github.com/dailydot/dailydot.com.git 
    cd dailydot.com
    virtualenv venv
    source venv/bin/activate
    pip install -U pip setuptools wheel
    pip install -r requirements.txt -r ./requirements/dev.txt

## Indexing for ElasticSearch (make sure ElasticSearch is running) Age is in hours

    python manage.py update_index --age=168 -v 2 -b 100 -k 4 -u default

## Starting the Django server

    python manage.py runserver 0.0.0.0:8000


Once you see, "Starting development server at http://0.0.0.0:8000/", 
visit [localhost:8000 in your browser](http://localhost:8000) to load it up. 
The first load may take a while, as the Redis cache may need to populate.


# Dependencies
---------------

| Area               |      Type      |      Package        |                                                        |
|--------------------|----------------|---------------------| -------------------------------------------------------|
| Support Libraries  | System Package | apt-get update      | Resynchronize the package index files and Upgrade the Debian Linux system including security update (Internet access required)|
|                    |                | build-essential     | Packages and Header files required for building system level software|
|                    |                | libxml2-dev         | Libraries, include files, etc you can use to developXML applications. This library allows to manipulate XMLIt includes support to read, modify and write HTML files. There is DTDs support this includes validation even with complex DtDs, either time or later once the document has been The output can be a simple SAX stream or and memory DOM like representations. In this case one the built-in XPath and XPointer implementation subnodes or ranges. A flexible Input/Output available, with existing HTTP and FTP combined to an URI library.|
|                    |                | libxslt1-dev        | XSLT is an XML language for defining transformations of files from XML to some other arbitrary format, such , HTML, plain text, etc. using standard XSLT libxslt is a C library which implements 1.0.|
|                    |                | libffi-dev          | This package contains the headers and static library files necessary for building programs which use libffi. function interface is the popular name for that allows code written in one language code written in another language. 
| Utilities          | System Package | curl                | A command line tool for getting or sending files using URL syntax. Since cURL uses libcurl, it supports a range of common Internet protocols, currently including TTP, HTTPS, FTP, FTPS, SCP, SFTP, TFTP, LDAP, DAP,ICT, TELNET, FILE, IMAP, POP3, SMTP and RTSP (the last four only in versions newer than 7.20.0 or 9 February 2010).|
|                    |                | npm                 | npm is a NodeJS package manager. As its name would imply, you can use it to install node programs. Also, if you use it in development, it makes it easier to specify and link dependencies.Sep 11, 2010|
|                    |                | wget                | GNU Wget (or just Wget, formerly Geturl) is a computer program that retrieves content from web servers. It is part of the GNU Project. Its name is derived from World Wide Web and get. It supports downloading via HTTP, HTTPS, and FTP protocols.|
|                    |                | pip                 | pip is a package management system used to install and manage software packages written in Python. Many packages can be found in the Python Package Index (PyPI). Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip (pip3 for Python 3) by default.|
|                    |                |                     |                                                        |
| Python-Core        | System Package | python-dev          | python-dev is the package that contains the header files for the Python C API, which is used by lxml because it includes Python C extensions for high performance.Jun 23, 2015|
|                    |                | python-virtualenv   | virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.|
|                    | Python Package | lxml                | lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language.|
|                    |                |                     |                                                        |
| 3rd Party Software | System Package | Heroku Cli          | The heroku command-line tool is an interface to the Heroku Platform API and includes support for things /renaming apps, running one-off dynos, , configuring add-ons and managing your . It’s generally installed in your local as part of the Heroku Toolbelt.|
|                    |                | PostgresSQL         | PostgreSQL (pronounced "post-gress-Q-L") is an open source relational database management system ( DBMS ) a worldwide team of volunteers. PostgreSQL controlled by any corporation or other private the source code is available free of charge.|
|                    |                | Tcl                 | Tcl (originally from Tool Command Language, but conventionally spelled "Tcl" rather than "TCL"; pronounced as "tickle" or "tee-see-ell"[4]) is a scripting language created by John Ousterhout.[5] Originally "born out of frustration",[6] according to the author, with programmers devising their own languages intended to be embedded into applications, Tcl gained acceptance on its own. It is commonly used for rapid prototyping, scripted applications, GUIs and testing. Tcl is used on embedded systems platforms, both in its full form and in several other small-footprint versions.|
|                    |                | Redis               | Redis is an open source (BSD licensed), in-memory data store, used as database, cache and message It supports data structures such as strings, lists, sets, sorted sets with range queries, hyperloglogs and geospatial indexes with.|
|                    |                | LessCSS             | Less is a CSS pre-processor, meaning that it extends the CSS language, adding features that allow variables, functions and many other techniques that allow make CSS that is more maintainable, themable and extendable.|
|                    |                | Java                | Java is a programming language and computing platform first released by Sun Microsystems in 1995. There are applications and websites that will not work have Java installed, and more are created . Java is fast, secure, and reliable.|
|                    |                | ElasticSearch       | Elasticsearch is a search server based on Lucene. It provides a distributed, multitenant-capable full-text with an HTTP web interface and free JSON documents. Elasticsearch is developed and is released as open source under the terms Apache License.|
|                    |                |                     |                                                        |

# Installing

### Installing Libraries

| Package            | Commands                                                            | 
|--------------------|---------------------------------------------------------------------|
| update             | ``` sudo apt-get update ```                                         |
| build-essential    | ``` sudo apt-get install build-essential ```                        |
| libxml2-dev        | ``` sudo apt-get install libxml2-dev ```                            |
| libxslt1-dev       | ``` sudo apt-get install libxslt1-dev ```                           |
| libffi-dev         | ``` sudo apt-get install libffi-dev ```                             |
|                    |                                                                     |

### Installing Utilities

| Package            | Commands                                                            |
|--------------------|---------------------------------------------------------------------|
| curl               | ``` sudo apt-get install curl ```                                   |
| npm                | ``` sudo apt-get install npm  ```                                   |
| wget               | ``` sudo apt-get install wget ```                                   |
| pip                | ``` sudo apt-get install python-pip ```                             |
|                    |                                                                     | 

### Installing Python-Core Additions

| Package            | Commands                                                            |
|--------------------|---------------------------------------------------------------------|
| python-dev         | ``` sudo apt-get install python-dev ```                             |         
| python-virtualenv  | ``` sudo apt-get install python-virtualenv ```                      |
| lxml               | ``` pip install lxml ```                                            |
|                    |                                                                     |

### Installing 3rd Party Software

| Package            | Commands                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Git                | ``` sudo apt-get install git ```                                                                |
| Heroku             | ``` wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh ```                             |
| PostgresSQL        | ``` sudo apt-get install postgresql-9.4 ```                                                     |
|                    | ``` sudo apt-get install postgresql-server-dev-9.4 ```                                          |
| Tcl                | ``` sudo apt-get install tcl8.5 ```                                                             |
| Redis - Manual Inst| ``` wget http://download.redis.io/redis-stable.tar.gz ```                                       |
|                    | ``` tar xvzf redis-stable.tar.gz  ```                                                           |
|                    | ``` cd redis-stable ```                                                                         |
|                    | ``` make ```                                                                                    |
|                    | ``` make test ```                                                                               |
|                    | ``` sudo make install ```                                                                       |
|                    | ``` cd utils ```                                                                                |
|                    | ``` sudo ./install_server.sh ```                                                                |
| Redis - apt-get    | ``` sudo apt-get install redis-server ```                                                       |
| LessCSS            | ``` sudo npm install -g less ```                                                                |
| Java               | ``` sudo apt-get install openjdk-8-jre ```                                                      |
| ElasticSearch      | ``` wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-2.3.1.tar.gz ``` |
|                    | ``` tar xzf elasticsearch-2.3.1.tar.gz  ```                                                     |
|                    | ``` sudo mv elasticsearch-2.3.1 /usr/share/elasticsearch ```                                    |

# Notes

## OS Issues

    Several flavors of Ubuntu were used during the creation of this note below are Issues that were discovered
 
    
|   Distribution       |  Version     |  Comments                                                  |
|----------------------|--------------|------------------------------------------------------------|
| Ubuntu               | 14.04        | The default Python version that sips with this distro is .7.6. This causes an issue with the ssl libraries of the modules and 3rd party addons. this issue is to hand build and install7.8 or above of python.|
|                      | 15.04        | The apt-get package for ElasticSearch while loads with-out error refuses to start. It gives no error or log entries. *** Additional investigation is required.***|
|                      | 15.10        | Durning the testing of this Distribution there was a fatal error that is currently unresolved.|

## Python:

    Python rev should be greater then 2.7.8
    
        
### Python Django-Nose

    Django-Nose is required to be installed into the virtualenv so It's not installed in the initial phases of the
    Python-Core updates.

{sre}
## Redis:

### Redis Ports
        
    Default server is at port 6379 once installed to start the server (Ubuntu 15.04)
   further
### Starting/Stopping Redis

#### Manual install start and stop

    sudo service redis_6379 start
    sudo service redis_6379 stop

#### apt-get install start stop instructions

    Currently while the server is starting it is returning a file not found error.
    *** This is still under investigation ***
    
    sudo service redis-server start
    sudo service redis-server start
    
### Testing Redis

    Stating the redis-cli is a good way to ensure you have the service up and
    running

    redis-cli
    redis 127.0.0.1:6379>

## ElasticSearch:

### Discoveries and Observations

    During the testing of these instructions the package available from Unbuntu loaded
    without incendent. However it failed to start the service. This is why the apt-get
    install instructions have been replaced with manual install & start instructions

{ses}
### Starting ElasticSearch

    cd /usr/share/elasticsearch
    ./bin/elasticsearch&

### Testing ElasticSearch
    curl  connect to http://localhost:9200

    curl localhost:9200

### Result should be

    {
        "status" : 200,
        "name" : "Tefral the Surveyor",
        "version" : {
          "number" : "1.0.3",
          "build_hash" : "NA",
          "build_timestamp" : "NA",
          "build_snapshot" : false,
          "lucene_version" : "4.6"
        },
        "tagline" : "You Know, for Search"
      }        
