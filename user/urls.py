from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.Register.as_view(), name='register'),
    path("login/", views.Login.as_view(), name='Login'),
    path("logout/", views.Logout.as_view(), name='Logout'),
]
