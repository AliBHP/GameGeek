"""GameGeek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from GamingGeek import views
from GamingGeek import userControlFuncions as usrFunc
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    # Django Basic
    path('admin/', admin.site.urls),

    # Navigation the site
    path('', views.home, name='index'),
    path('storehome/', views.MainPage, name='storeHome'),
    path('about/', views.about, name='about'),
    path('editUsers/', views.editUsers, name='editUsers'),

    # Create and deail with users
    path('loginRequest/', usrFunc.login, name='login'),
    path('addNewUser/', usrFunc.addNewUser, name='addNewUser'),
    path('register/', usrFunc.register, name='register'),

    # Function and work
    path('addItems/', views.addItems, name='addItems'),
    path('InsertNewItems/', views.InsertNewItems, name='InsertNewItems'),
    path('editStore/', views.editStore, name='editStore'),
    path('updateItem/', views.updateAnItem, name='updateItem'),
    path('updateUser/', views.updateUser, name='updateUser'),

    # Image uploading
    path('upload/', views.upload, name="upload"),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)