from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('accounts/login', views.user_login),
    path('accounts/register', views.user_register),
    path('accounts/logout', views.user_logout),
    path('about', views.about),
    path('articles', views.articles),
    path('articles/<page_id>', views.articles),
]