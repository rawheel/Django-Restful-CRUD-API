# Django-Restful-CRUD-API
Event Registration CRUD RestFul API 👾
### Fron End URL: https://github.com/rawheel/Event-Registration-App

<img src="https://miro.medium.com/max/1950/1*25Le7KoMK_z6BIaM8x74RA.png" alt="UMS">

## Project setup
```
pip install -r requirements.txt
```

### Compiles and hot-reloads for development
```
python manage.py runserver
```

## Tutorial
### STEP 1
Make sure you have python installed in your machine if not, you can install it from here in 2 mins. 
```
https://www.python.org/downloads/
```
### STEP 2
Install these dependencies/Libraries we'll be using them in the project.
```
Django==3.1.2
djangorestframework==3.12.4
django-cors-headers
```
You can install them by one by one ``` pip install  Django==3.1.2 ``` on your terminal or you can create a .txt file and paste all the required Libs with file name requirements.txt and run ``` pip install -r requirements.txt ``` It will install all the libraries at once.

SETUP IS DONE!😃

### STEP 3
Run this commnad on terminal in a particular folder to ``` Start django Project ```
```
django-admin startproject eventsapp
```
Now go into eventsapp folder and run
```
python manage.py runserver
```
The django project is working successfully! 🤞🏼

You'd be able to see this screen after searching your local server url ``` http://127.0.0.1:8000/ ``` on browser. 

<img src="https://d2gdtie5ivbdow.cloudfront.net/articles/quickstart-django/django_successful_install.png" alt="UMS">

Now create an app into django project by
```
python manage.py startapp CRUD
``` 

Now, Goto ``` eventsapp/setting.py ``` and add the app & lib in installed_apps ``` 'rest_framework','events' ```

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'events',
]
```

### STEP 5

Creating Models

```
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    community = models.CharField(max_length=15,default=None)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField(default=None)
    category = models.CharField(max_length=25)
    MODE_CHOICES=[
        ('phy',"Physical"),
        ('on',"Online")
    ]
    mode=models.CharField(choices=MODE_CHOICES,max_length=3)
    date_created = models.DateTimeField(auto_now=True,blank = True)

    class Meta:
        verbose_name_plural = 'events'
    def __str__(self):
        return self.title
```

Now, run these commands to save migrations

```
python manage.py makemigrations CRUD
```
```
python manage.py migrate
```

migrate, which is responsible for applying and unapplying migrations.

makemigrations, which is responsible for creating new migrations based on the changes you have made to your models.


### STEP 6
Create Superuser DJANGO-ADMIN
```
python manage.py createsuperuser
```
set your username and password.

Now, goto ``` CRUD/admin.py ``` then add

```
from .models import Event
admin.site.register(Event)
```

### STEP 7
create CRUD/serializers.py and add serializers
```
from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
```

### STEP 8
Add Views in CRUD/views.py
```
  
from django.shortcuts import render
from .models import Event
from .serializers import EventSerializer
from rest_framework import generics

class EventList(generics.ListCreateAPIView): # for just GET request
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
```

### STEP 9
Adding URLS

Goto ``` eventsapp/urls.py ``` and add
```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('CRUD.urls'))
```

Now, create a file in ``` CRUD/urls.py ``` and add
```
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [

    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetails.as_view()),
   
]
urlpatterns = format_suffix_patterns(urlpatterns)
```
Now, goto ``` http://127.0.0.1:8000/api/events/ ``` you can see something like this (not exactly like this but with your schema, you get it right?)

<img src="https://learndjango.com/static/images/tutorials/official_drf_tutorial_beginners_guide/hyperlink_snippet.png" alt="UMS">


Congratulations All is DONE, Create GET, POST, PUT, DELETE requests with your RESTFUL API! 😍

### STEP 10 (CORS Handling - optional)

Goto ``` eventsapp/settings.py ``` and add ``` 'corsheaders' ``` in installed_app
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'events',
    
    'corsheaders',
]
```
then,
Goto ``` eventsapp/settings.py ``` and add ``` 'corsheaders.middleware.CorsMiddleware' ``` in middleware

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'corsheaders.middleware.CorsMiddleware', 
]
```
Now, add this in settings.py
```
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
```

Great, Now you can host the app and access the api from any front end! 👨‍💻 


Developed by Raheel Siddiqui with 💚
