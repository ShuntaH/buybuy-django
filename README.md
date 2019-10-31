# BuyBuy-django
TO-BUY LIST APP

## Requirements
* Python3.7
* Django2.2
* Docker-compose
* PyCharm Professinal

## How to setup
```
git clone git@github.com:ShuntaH/buybuy-django.git

docker-compose up -d --build

docker exec -it alpine bin/ash/

# Don't access 0.0.0.0:8000. Use 172.0.0.1:8000 or localhost:8000
python manage.py runserver 0.0.0.0:8000

```

## PyCharm
setup interpreter and run configuration  

* Language & Framework -> Django

* Mark Enable Django

* Django Project Root -> project

* Settings -> project/project/settings.py

* Manage Script -> project/manage.py

* Execution -> Docker

* Run Configuration For Run and Debug -> Django Server

## Library
*  django-crispy-forms
https://django-crispy-forms.readthedocs.io/en/latest/

