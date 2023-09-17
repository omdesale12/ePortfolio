from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('test/', views.test, name="test"),
    path('eportfolio/usr/<str:email>/', views.eportfolio,name="eportfolio"),
]



 
