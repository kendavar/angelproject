"""angelproject URL Configuration

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
<<<<<<< HEAD
from django.conf.urls import path,url,include

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^angelapp/$',include("angelapp.urls"))
]
=======
from django.urls import url,include

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url('admin/', admin.site.urls),
    url(r'angelapp/',include('AppTwo.urls'))
]
>>>>>>> da9c7dcfe043aa48db7a1b6c558ebe240e01e471
