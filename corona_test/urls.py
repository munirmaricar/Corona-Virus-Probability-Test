from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('test', views.test, name='test'),
    path('result', views.result, name='result'),
    path('prevention', views.prevention, name='prevention'),
]