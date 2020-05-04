from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('result', views.result, name='result'),
    path('form', views.form, name='form'),
]