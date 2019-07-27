from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('accounts/login', views.user_login),
    path('accounts/register', views.user_register),
    path('accounts/logout', views.user_logout),
    path('accounts/user/<user_id>', views.users),
    path('about', views.about),
    path('articles', views.articles),
    path('articles/<int:page_id>', views.articles),
    path('article/<article_id>', views.article_info)
]

