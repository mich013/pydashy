Getting Started
===============

=====================

 

These are some basic survival instructions to get a local instance of
dailydot.com installed and running. Some elbow grease will need to be put into
making this easier and more portable. However, with these directions and some
luck, you'll be up and running!

 

Dependencies
------------

=========
---------

 

### Python:

Python rev should be greater then 2.7.6.

The reason is you will receive Insecure Platform Warnings and Errors from
various modules in Ubuntu 14.04 stock this causes a halt to the build process.

 

###       Required Python install packages



python-dev

python-virtualenv



###       Required Python Modules

lxml

django-nose



###       Utilities

curl

npm

wget

pip





### 3rd Party Packages

Heroku Cli

PostgresSQL

Redis

LessCSS

Java - required by ElasticSearch

ElasticSearch



### Support Libraries Required



libxml2-dev

libxslt1-dev

libffi-dev



 

Installation Instructions
-------------------------

 

 

###    Installing Utilities

 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install wget
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install curl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install python-pip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install npm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



###     Installing libararies



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install libxml2-dev
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install libxslt1-dev
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install libffi-dev
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





###      Python Update Installation



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install python-dev
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install python-virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



###      Python missing system modules install



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        pip install lxml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



###     Git Installation



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install git
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



###    Heroku Install Instructions

Link: https://toolbelt.heroku.com



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



###    PostgresSQL Install



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install postgresql-9.4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sudo apt-get install postgresql-server-dev-9.4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



\#\#\#    Redis Notes

\#\#\#        Default server is at port 6379

\#\#\#        once installed to start the server (Ubuntu 15.04)

'''

sudo service redis\_6379 start

sudo service redis\_6379 stop

'''



\#\#\#        Testing redis

\#\#\#            stating the redis-cli is a good way to ensure you have the
service up and running

'''

redis-cli

redis 127.0.0.1:6379\>

'''



\#\#\#    Redis Install

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

sudo ./install\_server.sh

'''



\#\#\#    LessCSS Install

'''

sudo apt-get install npm

sudo npm install -g less

'''

\#\#\#    Java Install

\#\#\#     Test if java is already installed

'''

java -version

\# if not install and atlest 1.8+

sudo apt-get install openjdk-8-jre

'''



\#\#\#    ElasticSearch Install

'''

wget
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-2.3.1.tar.gz

tar xzf elasticsearch-2.3.1.tar.gz

sudo mv elasticsearch-2.3.1 /usr/share/elasticsearch

cd /usr/share/elatsicsearch

sudo bin/elasticsearch&



\# starting ElasticSearch

cd /usr/share/elasticsearch

sudo ./bin/elasticsearch&

\# testing ElasticSearch

Using browser or curl  connect to http://localhost:9200

curl localhost:9200

\# result should be

{

"status" : 200,

"name" : "Tefral the Surveyor",

"version" : {

"number" : "1.0.3",

"build\_hash" : "NA",

"build\_timestamp" : "NA",

"build\_snapshot" : false,

"lucene\_version" : "4.6"

},

"tagline" : "You Know, for Search"

}

'''

 

\#\#\#     setting up build and venv

\#\#\#     clone repo

'''

git clone https://github.com/dailydot/dailydot.com.git

cd dailydot.com

virtualenv venv

venv/bin/pip install -U pip setuptools wheel

venv/bin/pip install -r requirements.txt

'''

 

\#\#\# setting up postgreSQL Daily Dot DB

\#\#\# Make Sure you login to heroku

'''

heroku login

'''

\#\#\# Obtain the snapshot. This will take a while!

'''

wget -O snapshot.dump \`heroku pg:backups public-url -q --app dailydot\`

'''

 

\#\#\# Create a database and load the snapshot into it

'''

createdb dailydot -T template0 -E UTF8

pg\_restore --verbose --clean --no-acl --no-owner -j 4 -d dailydot snapshot.dump

'''

\#\#\# Connect to the Daily Dot PostgreSQL database, change that user to

\#\#\# superuser, and grant it all privileges on all Daily Dot tables

'''

psql dailydot



alter user postgres superuser;

grant all privileges on all tables in schema public to postgres;

\#quit psql

'''



\#\#\# Activating the virtualenv

'''

source venv/bin/activate

'''

\#\#\# addiing Missing Django Requirement for Django-nose

'''

pip install django-nose

'''

 

\#\#\# Indexing for ElasticSearch (make sure ElasticSearch is running)

\#\#\# Age is in hours

'''

python manage.py update\_index --age=168 -v 2 -b 100 -k 4 -u default

'''

\#\#\# starting the Django server

'''

venv/bin/python manage.py runserver 0.0.0.0:8000

'''

\#\#\# Once you see, "Starting development server at http://0.0.0.0:8000/",
visit [localhost:8000 in your browser](http://localhost:8000) to load it up. The
first load may take a while, as the Redis cache may need to populate.