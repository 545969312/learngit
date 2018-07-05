"""many_table URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('query_book/', views.query_book, name='query_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('upload/', views.upload, name='upload'),
    re_path('del_book/(?P<dele>\d+)', views.del_book),
    re_path('change_book/(?P<change_id>\d+)', views.change_book)
]
