"""
URL configuration for Evisa project.

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
from django.urls import path, include

from Evisa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login,name="login"),
    path('home/',views.home,name="home"),
    path('verification/', views.passportverification, name="verification"),
    path('contact/',views.contact,name = "contact"),
    path('studentvisa/',views.studentvisa,name="student"),
    path('tourist/',views.tourist,name="tourist"),
    path('visarenewal/',views.visarenewal,name="renewal"),
    path('workvisa/',views.workvisa,name="workvisa"),
    path('',include('loginApp.urls')),
]
