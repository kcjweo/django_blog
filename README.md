# django_blog
This code is sample blog by django on docker container.

## 1. Start project

```linux
sudo docker-compose run web django-admin startproject django_blog
```

## 2. Start app

```linux
sudo docker-compose run web python3 django_blog/manage.py startapp django_blog_app
```

## 3. Migrate app

```linux
sudo docker-compose run web python3 django_blog/manage.py makemigrations
sudo docker-compose run web python3 django_blog/manage.py migrate
```

## 4. Start Web Server

```linux
sudo docker-compose up -d
```

## 5. Create Super User
```linux
sudo docker-compose run web python3 django_blog/manage.py createsuperuser
```