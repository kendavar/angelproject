<<<<<<< HEAD
from django.config.urls import url
from . import views

app_name = "angelapp"

urlpatterns = [
    url(r'^$',views.HomePage.as_view(),name='homepage')
=======
from django.conf.urls import url

app_name = 'angelapp'

urlpatterns = [
    url(r'profile/$',views.profile,name="profile")
>>>>>>> da9c7dcfe043aa48db7a1b6c558ebe240e01e471
]