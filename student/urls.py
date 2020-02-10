

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('registration/', views.registration),
    path('markslist/', views.markslist),
    path('marksview/', views.marksview),
    path('addstumarks/', views.StuMarks),
    path('alluser/', views.Users),
    path('home/', views.home),
    path('forgot_password/', views.password),
    path('^', views.index),
    path('mydetails/', views.details),
    path('fee/', views.fees),
    path('departments/', views.depart),
    path('presentfee/', views.presentfees),
    path('logout/', views.logout),
    path('staff/',views.staff_names),
    path('subject/',views.sub_name),
    path('staffdetails/',views.staffdetails),
    path('admin/', views.admin)
]


