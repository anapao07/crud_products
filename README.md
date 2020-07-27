# Project Title
Create, Read, Update, Delete Products
## Technologies 

- PostgreSQL 11
- Django 3.0
- rest framework
- HTML/CSS


## Installation

### Install PostgreSQL
#### - Crear Usuario Postgres
```
psql postgres
CREATE USER paola PASSWORD 'test1234';
```
#### - Create Database

```
CREATE DATABASE app_products WITH OWNER paola;
```

#### - Install  Python

```
sudp apt update
sudo apt install python3.8
```
#### - Install  pip
```
sudo apt install python3-pip
```
#### -  Install  Environment
```
sudo pip3 install virtualenv
```

### Steps to Start Project


####  1.- Clone Repository
```
git clone https://github.com/anapao07/crud_products.git

cd crud_products
```
#### 2.- Create and Activate Virtual Environment
```
virtualenv -p python3.8 crudenv
source crudenv/bin/activate
```

#### 3.- Install Requirements
```
pip install -r requirements.txt
```

#### 4.- Perform Migrations
```
python manage.py migrate
```
## Start Application
```
python manage.py runserver
```

### Api
```
http://0.0.0.0:8000/api/
```
### App
```
http://0.0.0.0:8000/
```

