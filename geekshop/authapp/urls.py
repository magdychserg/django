
from django.urls import path

import authapp
from authapp.views import login, register

app_name= 'authapp'
urlpatterns = [

    path('login', login, name='login'),
    path('register', register, name='register'),
]
