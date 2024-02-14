from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path('about', views.about, name='about'), # теперь url адрес вставляется автоматически при открытии страницы, т.е. теперь можно менять
   path('create', views.create, name='create')
]