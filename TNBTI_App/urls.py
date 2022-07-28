from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('manage-user/', views.manageUser, name="manage-user"),
    path('delete-user/<int:pk>/', views.deleteUser, name='delete-user'),
]
