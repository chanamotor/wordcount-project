from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage,name='home'),
    path('about/', views.about,name='about'),
    path('count/', views.count,name='count'),

]
