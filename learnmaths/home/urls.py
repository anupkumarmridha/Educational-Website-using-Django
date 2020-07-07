from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
   path('', views.home, name='home'),
   path('referenceBooks', views.referenceBooks, name='referenceBooks'),
   path('videos', views.videos, name='videos'),
   path('about', views.about, name='about'),
   path('contact', views.contact, name='contact'),
   path('search', views.search, name='search'),
   path('singup', views.handelSingup, name='handelSingup')
   

]