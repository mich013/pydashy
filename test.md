# Getting Started
===============

These are some basic survival instructions to get a local instance of dailydot.com
installed and running. Some elbow grease will need to be put into making this easier
and more portable. However, with these directions and some luck, you'll be up and
running!

If this is a clean and fresh build install please be sure to read the
[dependency section](#dependencies) to insure installation of all required software,
modules and libraries.


# Creating and Building Instance

## Database downloading and importing

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
    venv/bin/pip install -U pip setuptools wheel
    venv/bin/pip install -r requirements.txt

## Activating the virtualenv

    source venv/bin/activate

## Adding Missing Django Requirement for Django-nose

    pip install django-nose

## Indexing for ElasticSearch (make sure ElasticSearch is running) Age is in hours

    python manage.py update_index --age=168 -v 2 -b 100 -k 4 -u default

## Starting the Django server

    venv/bin/python manage.py runserver 0.0.0.0:8000


Once you see, "Starting development server at http://0.0.0.0:8000/", 
visit [localhost:8000 in your browser](http://localhost:8000) to load it up. 
The first load may take a while, as the Redis cache may need to populate.


# Dependencies
---------------

| Area               |      Type      |      Package        |                                                        |
|--------------------|----------------|---------------------| -------------------------------------------------------|
| Python-Core        | System Package | python-dev          | python-dev is the package that contains the header     |
|                    |                |                     | files for the Python C API, which is used by lxml      |
|                    |                |                     | because it includes Python C extensions for high       |
|                    |                |                     | performance.Jun 23, 2015                               |
|                    |                |                     |                                                        |
|                    |                | python-virtualenv   | virtualenv is a tool to create isolated Python         |
|                    |                |                     | environments. virtualenv creates a folder which        |
|                    |                |                     | contains all the necessary executables to use the      |
|                    |                |                     | packages that a Python project would need.             |
|                    |                |                     |                                                        |
|                    | Python Package | lxml                | lxml is the most feature-rich and easy-to-use library  |
|                    |                |                     | for processing XML and HTML in the Python language.    |
|                    |                |                     |                                                        |
|                    |                | django-nose         | django-nose provides all the goodness of nose in your  |
|                    |                |                     | Django tests, like: Testing just your apps by default, |
|                    |                |                     | not all the standard ones that happen to be in         |
|                    |                |                     | INSTALLED_APPS. Running the tests in one or more       |
|                    |                |                     | specific modules (or apps, or classes, or folders, or  |
|                    |                |                     | just running a specific test)                          |
|                    |                |                     |                                                        | 
| Utilities          | System Package | curl                | A command line tool for getting or sending files using |
|                    |                |                     | URL syntax. Since cURL uses libcurl, it supports a     |
|                    |                |                     | range of common Internet protocols, currently including|
|                    |                |                     | HTTP, HTTPS, FTP, FTPS, SCP, SFTP, TFTP, LDAP, DAP,    |
|                    |                |                     | DICT, TELNET, FILE, IMAP, POP3, SMTP and RTSP          |
|                    |                |                     | (the last four only in versions newer than 7.20.0 or 9 |
|                    |                |                     | February 2010).                                        |
|                    |                |                     |                                                        |
|                    |                | npm                 | npm is a NodeJS package manager. As its name would     |
|                    |                |                     | imply, you can use it to install node programs. Also,  |
|                    |                |                     | if you use it in development, it makes it easier to    |
|                    |                |                     | specify and link dependencies.Sep 11, 2010             |
|                    |                |                     |                                                        |
|                    |                | wget                | GNU Wget (or just Wget, formerly Geturl) is a computer |
|                    |                |                     | program that retrieves content from web servers. It is |
|                    |                |                     | part of the GNU Project. Its name is derived from World|
|                    |                |                     | Wide Web and get. It supports downloading via HTTP,    |
|                    |                |                     | HTTPS, and FTP protocols.                              |
|                    |                |                     |                                                        |
|                    |                | pip                 | pip is a package management system used to install     |
|                    |                |                     | and manage software packages written in Python.        |
|                    |                |                     | Many packages can be found in the Python Package Index |
|                    |                |                     | (PyPI). Python 2.7.9 and later                         |
|                    |                |                     | (on the python2 series), and Python 3.4 and later      |
|                    |                |                     | include pip (pip3 for Python 3) by default.            |
|                    |                |                     |                                                        |
| 3rd Party Software | System Package | Heroku Cli          | The heroku command-line tool is an interface to the    |
|                    |                |                     | Heroku Platform API and includes support for things    |
|                    |                |                     | like creating/renaming apps, running one-off dynos,    |
|                    |                |                     | taking backups, configuring add-ons and managing your  |
|                    |                |                     | app’s state. It’s generally installed in your local    |
|                    |                |                     | dev environment as part of the Heroku Toolbelt.        |
|                    |                |                     |                                                        |
|                    |                | PostgresSQL         | PostgreSQL (pronounced "post-gress-Q-L") is an open    |
|                    |                |                     | source relational database management system ( DBMS )  |
|                    |                |                     | developed by a worldwide team of volunteers. PostgreSQL|
|                    |                |                     | is not controlled by any corporation or other private  |
|                    |                |                     | entity and the source code is available free of charge.|
|                    |                |                     |                                                        |
|                    |                | Redis               | Redis is an open source (BSD licensed), in-memory data |
|                    |                |                     | structure store, used as database, cache and message   |
|                    |                |                     | broker. It supports data structures such as strings,   |
|                    |                |                     | hashes, lists, sets, sorted sets with range queries,   |
|                    |                |                     | bitmaps, hyperloglogs and geospatial indexes with      |
|                    |                |                     | radius queries.                                        |
|                    |                |                     |                                                        |
|                    |                | LessCSS             | Less is a CSS pre-processor, meaning that it extends   |
|                    |                |                     | the CSS language, adding features that allow variables,|
|                    |                |                     | mixins, functions and many other techniques that allow |
|                    |                |                     | you to make CSS that is more maintainable, themable and|
|                    |                |                     | extendable.                                            |
|                    |                |                     |                                                        |
|                    |                | Java                | Java is a programming language and computing platform  |
|                    |                |                     | first released by Sun Microsystems in 1995. There are  |
|                    |                |                     | lots of applications and websites that will not work   |
|                    |                |                     | unless you have Java installed, and more are created   |
|                    |                |                     | every day. Java is fast, secure, and reliable.         |
|                    |                |                     |                                                        |
|                    |                | ElasticSearch       | Elasticsearch is a search server based on Lucene. It   |
|                    |                |                     | provides a distributed, multitenant-capable full-text  |
|                    |                |                     | search engine with an HTTP web interface and           |
|                    |                |                     | schema-free JSON documents. Elasticsearch is developed |
|                    |                |                     | in Java and is released as open source under the terms |
|                    |                |                     | of the Apache License.                                 |
|                    |                |                     |                                                        |
| Support Libraries  | System Package | libxml2-dev         | Libraries, include files, etc you can use to develop   |
|                    |                |                     | XML applications. This library allows to manipulate XML|
|                    |                |                     | files. It includes support to read, modify and write   |
|                    |                |                     | XML and HTML files. There is DTDs support this includes|
|                    |                |                     | parsing and validation even with complex DtDs, either  |
|                    |                |                     | at parse time or later once the document has been      |
|                    |                |                     | modified. The output can be a simple SAX stream or and |
|                    |                |                     | in-memory DOM like representations. In this case one   |
|                    |                |                     | can use the built-in XPath and XPointer implementation |
|                    |                |                     | to select subnodes or ranges. A flexible Input/Output  |
|                    |                |                     | mechanism is available, with existing HTTP and FTP     |
|                    |                |                     | modules and combined to an URI library.                |
|                    |                |                     |                                                        |
|                    |                | libxslt1-dev        | XSLT is an XML language for defining transformations of|
|                    |                |                     | XML files from XML to some other arbitrary format, such|
|                    |                |                     | as XML, HTML, plain text, etc. using standard XSLT     |
|                    |                |                     | stylesheets. libxslt is a C library which implements   |
|                    |                |                     | XSLT version 1.0.                                      |
|                    |                |                     |                                                        |
|                    |                | libffi-dev          | This package contains the headers and static library   |
|                    |                |                     | files necessary for building programs which use libffi.|
|                    |                |                     | A foreign function interface is the popular name for   |
|                    |                |                     | the interface that allows code written in one language |
|                    |                |                     | to call code written in another language.              |
|                    |                |                     |                                                        |
| 3rd Party Software | System Package | Heroku Cli          | The heroku command-line tool is an interface to the    |
|                    |                |                     | Heroku Platform API and includes support for things    |
|                    |                |                     | like creating/renaming apps, running one-off dynos,    |
|                    |                |                     | taking backups, configuring add-ons and managing your  |
|                    |                |                     | app’s state. It’s generally installed in your local    |
|                    |                |                     | dev environment as part of the Heroku Toolbelt.        |
|                    |                |                     |                                                        |
|                    |                | PostgresSQL         | PostgreSQL (pronounced "post-gress-Q-L") is an open    |
|                    |                |                     | source relational database management system ( DBMS )  |
|                    |                |                     | developed by a worldwide team of volunteers. PostgreSQL|
|                    |                |                     | is not controlled by any corporation or other private  |
|                    |                |                     | entity and the source code is available free of charge.|
|                    |                |                     |                                                        |
|                    |                | Redis               | Redis is an open source (BSD licensed), in-memory data |
|                    |                |                     | structure store, used as database, cache and message   |
|                    |                |                     | broker. It supports data structures such as strings,   |
|                    |                |                     | hashes, lists, sets, sorted sets with range queries,   |
|                    |                |                     | bitmaps, hyperloglogs and geospatial indexes with      |
|                    |                |                     | radius queries.                                        |
|                    |                |                     |                                                        |
|                    |                | LessCSS             | Less is a CSS pre-processor, meaning that it extends   |
|                    |                |                     | the CSS language, adding features that allow variables,|
|                    |                |                     | mixins, functions and many other techniques that allow |
|                    |                |                     | you to make CSS that is more maintainable, themable and|
|                    |                |                     | extendable.                                            |
|                    |                |                     |                                                        |
|                    |                | Java                | Java is a programming language and computing platform  |
|                    |                |                     | first released by Sun Microsystems in 1995. There are  |
|                    |                |                     | lots of applications and websites that will not work   |
|                    |                |                     | unless you have Java installed, and more are created   |
|                    |                |                     | every day. Java is fast, secure, and reliable.         |
|                    |                |                     |                                                        |
|                    |                | ElasticSearch       | Elasticsearch is a search server based on Lucene. It   |
|                    |                |                     | provides a distributed, multitenant-capable full-text  |
|                    |                |                     | search engine with an HTTP web interface and           |
|                    |                |                     | schema-free JSON documents. Elasticsearch is developed |
|                    |                |                     | in Java and is released as open source under the terms |
|                    |                |                     | of the Apache License.                                 |
|                    |                |                     |                                                        |
| Support Libraries  | System Package | libxml2-dev         | Libraries, include files, etc you can use to develop   |
|                    |                |                     | XML applications. This library allows to manipulate XML|
|                    |                |                     | files. It includes support to read, modify and write   |
|                    |                |                     | XML and HTML files. There is DTDs support this includes|
|                    |                |                     | parsing and validation even with complex DtDs, either  |
|                    |                |                     | at parse time or later once the document has been      |
|                    |                |                     | modified. The output can be a simple SAX stream or and |
|                    |                |                     | in-memory DOM like representations. In this case one   |
|                    |                |                     | can use the built-in XPath and XPointer implementation |
|                    |                |                     | to select subnodes or ranges. A flexible Input/Output  |
|                    |                |                     | mechanism is available, with existing HTTP and FTP     |
|                    |                |                     | modules and combined to an URI library.                |
|                    |                |                     |                                                        |
|                    |                | libxslt1-dev        | XSLT is an XML language for defining transformations of|
|                    |                |                     | XML files from XML to some other arbitrary format, such|
|                    |                |                     | as XML, HTML, plain text, etc. using standard XSLT     |
|                    |                |                     | stylesheets. libxslt is a C library which implements   |
|                    |                |                     | XSLT version 1.0.                                      |
|                    |                |                     |                                                        |
|                    |                | libffi-dev          | This package contains the headers and static library   |
|                    |                |                     | files necessary for building programs which use libffi.|
|                    |                |                     | A foreign function interface is the popular name for   |
|                    |                |                     | the interface that allows code written in one language |
|                    |                |                     | to call code written in another language.              |
|                    |                |                     |                                                        |

### Installing Python-Core Additions

| Package            | Commands                                                            |
|--------------------|---------------------------------------------------------------------|
| python-dev         | ``` sudo apt-get install python-dev ```                             |         
| python-virtualenv  | ``` sudo apt-get install python-virtualenv ```                      |
| lxml               | ``` pip install lxml ```                                            |
|                    |                                                                     |

### Installing Utilities

| Package            | Commands                                                            |
|--------------------|---------------------------------------------------------------------|
| curl               | ``` sudo apt-get install curl ```                                   |
| npm                | ``` sudo apt-get install npm  ```                                   |
| wget               | ``` sudo apt-get install wget ```                                   |
| pip                | ``` sudo apt-get install python-pip ```                             |
|                    |                                                                     | 
        
### Installing Libraries

| Package            | Commands                                                            | 
|--------------------|---------------------------------------------------------------------|
| libxml2-dev        | ``` sudo apt-get install libxml2-dev ```                            |
| libxslt1-dev       | ``` sudo apt-get install libxslt1-dev ```                           |
| libffi-dev         | ``` sudo apt-get install libffi-dev ```                             |
|                    |                                                                     |


### Installing 3rd Party Software

| Package            | Commands                                                                                        |
|--------------------|-------------------------------------------------------------------------------------------------|
| Git                | ``` sudo apt-get install git ```                                                                |
| Heroku             | ``` wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh ```                             |
| PostgresSQL        | ``` sudo apt-get install postgresql-9.4 ```                                                     |
|                    | ``` sudo apt-get install postgresql-server-dev-9.4 ```                                          |
| Redis              | ``` sudo apt-get update ```                                                                     |
|                    | ``` sudo apt-get install build-essential ```                                                    |
|                    | ``` sudo apt-get install tcl8.5 ```                                                             |
|                    | ``` wget http://download.redis.io/redis-stable.tar.gz ```                                       |
|                    | ``` tar xvzf redis-stable.tar.gz                                                                |
|                    | ``` cd redis-stable ```                                                                         |
|                    | ``` make                                                                                        |
|                    | ``` make test ```                                                                               |
|                    | ``` sudo make install ```                                                                       |
|                    | ``` cd utils ```                                                                                |
|                    | ``` sudo ./install_server.sh ```                                                                |
| LessCSS            | ``` sudo npm install -g less ```                                                                |
| Java               | ``` sudo apt-get install openjdk-8-jre ```                                                      |
| ElasticSearch      | ``` wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-2.3.1.tar.gz ``` |
|                    | ``` tar xzf elasticsearch-2.3.1.tar.gz  ```                                                     |
|                    | ``` sudo mv elasticsearch-2.3.1 /usr/share/elasticsearch ```                                    |

# Notes

## Python:

        Python rev should be greater then 2.7.6
        The reason is you will receive Insecure Platform Warnings and Errors from various modules in Ubuntu 
        14.04 stock this causes a halt to the build process.


## Redis:

### Redis Ports
        Default server is at port 6379 once installed to start the server (Ubuntu 15.04)
        
### Starting/Stopping Redis

        ```
        sudo service redis_6379 start
        sudo service redis_6379 stop
        ```
        
### Testng redis

        Stating the redis-cli is a good way to ensure you have the service up and
        running

        ```
        redis-cli
        redis 127.0.0.1:6379>
        ```

## ElasticSearch

### Starting ElasticSearch

        ```
        cd /usr/share/elasticsearch
        sudo ./bin/elasticsearch&
        ```

### Testing ElasticSearch Using browser or curl  connect to http://localhost:9200

        ```
        curl localhost:9200
        ```

### Result should be

        ```
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
        ```

# old version Below

# Getting Started
===============

        These are some basic survival instructions to get a local instance of dailydot.com installed and running. 
        Some elbow grease will need to be put into making this easier and more portable. However, with these 
        directions and some luck, you'll be up and running!

## Required Python install packages

* python-dev
* python-virtualenv

## Required Python Modules

* lxml
* django-nose

### Utilities

* curl
* npm
* wget
* pip

### 3rd Party Packages

* Heroku Cli
* PostgresSQL
* Redis
* LessCSS
* Java - required by ElasticSearch
* ElasticSearch



### Support Libraries Required

* libxml2-dev
* libxslt1-dev
* libffi-dev

### Installation Instructions
-------------------------

## Installing Utilities

```
        sudo apt-get install wget
        sudo apt-get install curl
        sudo apt-get install python-pip
        sudo apt-get install npm
```

## Installing libararies

```
        sudo apt-get install libxml2-dev
        sudo apt-get install libxslt1-dev
        sudo apt-get install libffi-dev
```

## Python Update Installation

```
        sudo apt-get install python-dev
        sudo apt-get install python-virtualenv
```

## Python missing system modules install

```
        pip install lxml
```        

## Git Installation

```
        sudo apt-get install git
```

## Heroku Install Instructions

        Link: https://toolbelt.heroku.com

```
        wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```

## PostgresSQL Install

```

        sudo apt-get install postgresql-9.4
        sudo apt-get install postgresql-server-dev-9.4
```

## Redis Notes

        Default server is at port 6379 once installed to start the server (Ubuntu 15.04)

```
        sudo service redis_6379 start
        sudo service redis_6379 stop
```

## Testing redis

        Stating the redis-cli is a good way to ensure you have the service up and
        running

```
        redis-cli
        redis 127.0.0.1:6379>
```

## Redis Install

```
        sudo apt-get update
        sudo apt-get install build-essential
        sudo apt-get install tcl8.5
        wget http://download.redis.io/redis-stable.tar.gz
        tar xvzf redis-stable.tar.gz
        cd redis-stable
        make
        make test
        sudo make install
        cd utils
        sudo ./install_server.sh
```

## LessCSS Install

```

        sudo apt-get install npm
        sudo npm install -g less
```

## Java Install
        Test if java is already installed


```
        java -version
        # if not install and atlest 1.8+
        sudo apt-get install openjdk-8-jre
```

## ElasticSearch Install

```
        wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-2.3.1.tar.gz
        tar xzf elasticsearch-2.3.1.tar.gz
        sudo mv elasticsearch-2.3.1 /usr/share/elasticsearch
```

`


### Setting up build and Virtialenv

## Clone repo

```
        git clone https://github.com/dailydot/dailydot.com.git
        cd dailydot.com
        virtualenv venv
        venv/bin/pip install -U pip setuptools wheel
        venv/bin/pip install -r requirements.txt 
```

## Setting up postgreSQL Daily Dot DB (Make Sure you login to heroku)

```
        heroku login
```

## Obtain the snapshot. This will take a while!

```
        wget -O snapshot.dump `heroku pg:backups public-url -q --app dailydot`
```

## Create a database and load the snapshot into it

```
        createdb dailydot -T template0 -E UTF8
        pg_restore --verbose --clean --no-acl --no-owner -j 4 -d dailydot snapshot.dump
```

## Connect to the Daily Dot PostgreSQL database, change that user to superuser, and grant it all privileges on all Daily Dot tables

```

        psql dailydot
        alter user postgres superuser;
        grant all privileges on all tables in schema public to postgres;
        (quit psql)
```

## Activating the virtualenv

```
        source venv/bin/activate
```

## Adding Missing Django Requirement for Django-nose

```
        pip install django-nose
```

## Indexing for ElasticSearch (make sure ElasticSearch is running) Age is in hours

```
python manage.py update_index --age=168 -v 2 -b 100 -k 4 -u default
```

## Starting the Django server

```
        venv/bin/python manage.py runserver 0.0.0.0:8000
```

## Once you see, "Starting development server at http://0.0.0.0:8000/", 
visit [localhost:8000 in your browser](http://localhost:8000) to load it up. 
The first load may take a while, as the Redis cache may need to populate.






### Getting Started
### =================

### These are some basic survival instructions to get a local instance of dailydot.com installed and running. Some elbow grease will need to be put into making this easier and more portable. However, with these directions and some luck, you'll be up and running!


### Dependencies

### Python:
###    Python rev should be greater then 2.7.6.
###    The reason is you will receive Insecure Platform Warnings and Errors
###    from various modules in Ubuntu 14.04 stock this causes a halt to the build process.
###    
###    Required Python install packages
###    
###        python-dev
###        python-virtualenv
###        
###    Required Python Modules
###        lxml
###        django-nose
    
### Utilities
###    curl
###    npm
###    wget
###    pip
    
        
### 3rd Party Packages
###    Heroku Cli
###    PostgresSQL
###    Redis
###    LessCSS
###    Java - required by ElasticSearch
###    ElasticSearch
    
### Support Libraries Required
    
###    libxml2-dev
###    libxslt1-dev
###    libffi-dev
    

### Installation Instructions
###
###    Installing Utilities
    '''
        sudo apt-get install wget
        sudo apt-get install curl
        sudo apt-get install python-pip
        sudo apt-get install npm
    '''
        
###    Installing libararies
    '''
        sudo apt-get install libxml2-dev
        sudo apt-get install libxslt1-dev
        sudo apt-get install libffi-dev
    '''
    
###    Python Update Installation
    '''
        sudo apt-get install python-dev
        sudo apt-get install python-virtualenv
    '''    
###    Python missing system modules install
    '''
        pip install lxml
    '''
###    Git Installation
    '''
        sudo apt-get install git
    ''' 
###    Heroku Install Instructions
###        Link: https://toolbelt.heroku.com
    '''
        wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
    ''' 
###    PostgresSQL Install
    '''
        sudo apt-get install postgresql-9.4
        sudo apt-get install postgresql-server-dev-9.4
    ''' 
###    Redis Notes
###        Default server is at port 6379
###        once installed to start the server (Ubuntu 15.04)
    '''
        sudo service redis_6379 start
        sudo service redis_6379 stop
    '''
            
###        Testing redis
###            stating the redis-cli is a good way to ensure you have the service up and running
    '''
        redis-cli
        redis 127.0.0.1:6379>
    '''
    
###    Redis Install
    '''
        sudo apt-get update
        sudo apt-get install build-essential
        sudo apt-get install tcl8.5
        wget http://download.redis.io/redis-stable.tar.gz
        tar xvzf redis-stable.tar.gz
        cd redis-stable
        make
        make test
        sudo make install
        cd utils
        sudo ./install_server.sh
    '''
    
###    LessCSS Install
    '''
        sudo apt-get install npm
        sudo npm install -g less
    ''' 
###    Java Install
###     Test if java is already installed
    '''
        java -version
        # if not install and atlest 1.8+
        sudo apt-get install openjdk-8-jre
    '''
        
###    ElasticSearch Install
    '''
        wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-2.3.1.tar.gz
        tar xzf elasticsearch-2.3.1.tar.gz
        sudo mv elasticsearch-2.3.1 /usr/share/elasticsearch
        cd /usr/share/elatsicsearch
        sudo bin/elasticsearch&
        
        # starting ElasticSearch
        cd /usr/share/elasticsearch
        sudo ./bin/elasticsearch&
        # testing ElasticSearch
        Using browser or curl  connect to http://localhost:9200
        curl localhost:9200
        # result should be
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
    '''

###     setting up build and venv
###     clone repo
    '''
        git clone https://github.com/dailydot/dailydot.com.git
        cd dailydot.com
        virtualenv venv
        venv/bin/pip install -U pip setuptools wheel
        venv/bin/pip install -r requirements.txt 
    '''

### setting up postgreSQL Daily Dot DB
### Make Sure you login to heroku
    '''
        heroku login
    '''
### Obtain the snapshot. This will take a while!
    '''
        wget -O snapshot.dump `heroku pg:backups public-url -q --app dailydot`
    '''

### Create a database and load the snapshot into it
    '''
        createdb dailydot -T template0 -E UTF8
        pg_restore --verbose --clean --no-acl --no-owner -j 4 -d dailydot snapshot.dump
    '''
### Connect to the Daily Dot PostgreSQL database, change that user to
### superuser, and grant it all privileges on all Daily Dot tables
    '''
        psql dailydot
        
            alter user postgres superuser;
            grant all privileges on all tables in schema public to postgres;
            #quit psql
    '''
        
### Activating the virtualenv
    '''
        source venv/bin/activate
    '''
### addiing Missing Django Requirement for Django-nose
    '''
        pip install django-nose
    '''

### Indexing for ElasticSearch (make sure ElasticSearch is running)
### Age is in hours
    '''
        python manage.py update_index --age=168 -v 2 -b 100 -k 4 -u default
    '''
### starting the Django server
    '''
        venv/bin/python manage.py runserver 0.0.0.0:8000
    '''
### Once you see, "Starting development server at http://0.0.0.0:8000/", visit [localhost:8000 in your browser](http://localhost:8000) to load it up. The first load may take a while, as the Redis cache may need to populate.
