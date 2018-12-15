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
#<<<<<<< HEAD
from django.urls import path,include
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/login/')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('angelapp/',include('angelapp.urls'))
    
# #=======
# #from angelapp import views
# from django.urls import path, include,re_path

# #urlpatterns = [
# #    path('admin/', admin.site.urls),
# #    re_path(r'^$',views.HomePage.as_view(),name='homepage'),
# #    re_path(r'^angelapp/',include("angelapp.urls")),
# #    path('accounts/', include('django.contrib.auth.urls'))
# #>>>>>>> e671e54a0bbc2726c7dec09c91f37eea12271ccb
]


# Username (leave blank to use 'kentheangel'): angel
# Email address: kendarules@gmail.com
# Password: Kaneki3kenda
