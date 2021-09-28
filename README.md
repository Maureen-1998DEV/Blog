# Personal-Blog

 By [Maureen Akinyi Ougo](https://Maureen-1998DEV.github.io/Portfolio/)

## User Requirements

+ [x] As a user I would like to view the blog posts submitted
+ [x] As a user I would like to comment on blog posts
+ [x] As a user I would like to view the most recent posts
+ [x] As a user I would like to alerted when a new post is made by joining a subscription.

## Writer Requirements

+ [x] As a writer I would like to sign in to the blog.
+ [x] As a writer I would also like to create blog from the application.
+ [x] As a writer I would like to delete comments that I find insulting or degrading.
+ [x] As a writer I would like to update or delete blogs i have created.


## Specifications

[SPECS.md](https://github.com/Maureen-1998DEV/blog/blob/master/specs.md)

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.

* Python 3.8

### Cloning the repository

```git clone https://github.com/Maureen-1998DEV/Blog.git```


### Database migrations

```bash
# first initialize the database if the migrations folder does not exist
python manage.py db init
# create  a migration
python manage.py db migrate -m "initial migration"
# upgrade
python manage.py db upgrade
# insert initial data
python manage.py insert_initial_data
```

### Installing dependencies

```
pip3 install -r requirements
```

### Prepare environmet variables

In start.sh file, in the root folder

```bash
 export MAIL_USERNAME=YOUR EMAIL
 export MAIL_PASSWORD=EMAIL PASSWORD
 export ADMIN_MAIL_USERNAME=ADMIN ACCOUNT EMAIL
```



### Creating a virtual environment

```
python3.8 -m virtualenv virtual-blog
source virtual-blog/bin/activate
```
### Running Tests

```bash
python3.8 manage.py test
```


## Live Demo

The web app can be accessed from the following link
[https://ougoblog.herokuapp.com/](click here)


## Technology used

* [Python3.8](https://www.python.org/)

* [Flask](http://flask.pocoo.org/)

* [Heroku](https://heroku.com)

* [Bootstrap](https://bootstrapcdn.com)

## Contributing

- Git clone [https://github.com/Maureen-1998DEV/Blog.git](https://github.com/Maureen-1998DEV/Blog.git) 


MIT License

Copyright (c) [2021] [Maureen Akinyi Ougo]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.