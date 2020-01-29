

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('registration/', views.registration),
    path('markslist/', views.markslist),
    path('marksview/', views.marksview),
    path('addstumarks/', views.StuMarks),
    path('allusers/', views.Users),
    path('home/', views.home),
    path('^', views.index),
    path('mydetails/',views.details),
]


