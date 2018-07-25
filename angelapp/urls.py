from django.config.urls import url
from . import views

app_name = "angelapp"

urlpatterns = [
    url(r'^$',views.HomePage.as_view(),name='homepage')
]