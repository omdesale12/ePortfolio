from django.urls import path,include
from . import views
urlpatterns = [
    path('register/', views.register, name="register"),
    path('loginUser/', views.loginUser, name="loginUser"),
    path('logoutUser/', views.logoutUser, name="logoutUser"),
    path('profile/<str:user_id>',views.profile,name="profile"),
    path('updateProfile/<str:user_id>',views.updateProfile,name="updateProfile"),
    path('portfolio_details/<str:user_id>',views.portfolio_details,name="viewPortfolio"),
    path('addPortfolio/', views.addPortfolio, name="addPortfolio"),
    path('addResume/', views.addResume, name="addResume"),

]


