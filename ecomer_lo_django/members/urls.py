from django.urls import path
from .import views

urlpatterns= [
    path('members/', views.members , name='members'),
    path('template/', views.mysecond , name='template'),
    path('template3/',views.testing, name= 'template3'),
]