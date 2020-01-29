

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('registration/', views.registration),
    path('markslist/', views.markslist),
    path('marksview/', views.marksview),
    path('addstumarks/', views.StuMarks),
    path('my_details/', views.details),
    path('allusers/', views.Users),
    path('home/', views.home),
    path('^', views.index),
]


