from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('success', success, name="success"),
    path('token', token, name="token"),
    path('verify/<auth_token>', verification, name="verification"),
    path('error', error, name="error"),
]