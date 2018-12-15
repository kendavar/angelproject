from django.urls import path
from django.views.generic.base import TemplateView
from . import views
app_name = 'angelapp'

urlpatterns = [
    #path('home/', TemplateView.as_view(template_name='home.html'), name='homie'),
    path(r'', views.List_user_page.as_view(), name='home'),
    path(r'<int:pk>', views.detailView.as_view(), name='detail'),
    path('home/', views.homePageView, name='home'),
    #the address targetted at the MainActivity.java file. It was the destination where Volley has to send data
    path(r'insert/', views.fcm_insert, name='insert'),
    #for sending the notification
    path(r'send/(?P<value>\s+)/$', views.send_notifications, name='send')
]

