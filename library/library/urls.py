"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from record.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book_list, name='book-list'),
    path('authors/', authors_list, name='author-list'),
    path('copies/', copies_list, name='copies-list'),
    path('borrowers/', borrower_list, name='borrower-list'),
    path('branch/', branch_list, name='branch-list'),
    path('loans/', loans_list, name='loan-list'),
    path('publisher/', publisher_list, name='publisher-list'),
    path('bookcopiesatallbranches/', bookcopiesatallbranches_procedure, name='bookcopiesatallbranches')

]
