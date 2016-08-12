# CultureIQ Code Challenge

Welcome to my project for the CultureIQ Code Challenge. The challenge was to create a web application that took in text, determined the language, translated it, and then showed the translation to the user and stored everything in a database.

An example instance of this project can be viewed [here](http://54.173.58.137/). Which is currently hosted on AWS.

Thank you to CultureIQ for the cool challenge and for the opportunity to start learning a new web framework.

## Technology Stack
Web Server: Nginx

Database: PostgreSQL

Web Framework: Django

Frontend Framework: AngularJS

## Installation and setup

Must install the python packages `langdetect` and `google-api-python-client`


Add json config files to cultureiq/config/db_config.json and translator/config/google_api.json

Example db config (cultureiq/config/db_config.json):

```
{
  "NAME": "dbname",
  "USER": "user",
  "PASSWORD": "userpass",
  "HOST": "127.0.0.1",
  "PORT": "5432"
}
```

Example google api file (translator/config/google_api.json):

```
{
  "API_TOKEN": "myAPItoken"
}
```
