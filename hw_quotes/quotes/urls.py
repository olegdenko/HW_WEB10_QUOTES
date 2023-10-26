from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name="root"),
    path("upload/", views.upload, name="upload"),
    path('author/<str:author_id>/', views.author_detail, name='author_detail'),
    path("quotes/", views.main, name="quotes"),
    path("quotes/edit/<int:pic_id>", views.edit, name="edit"),
    path("quotes/remove/<int:pic_id>", views.remove, name="remove"),
    path('<int:page>', views.main, name="root_paginate"),
    path("login/", views.login, name="SignIn"),
    path('tag/<str:tag>/', views.tag_quotes, name='tag_quotes')
]
