from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name ="delete"),
    path('check/<int:pk>/', views.check, name="check"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('register/', views.registerView, name='register')
]