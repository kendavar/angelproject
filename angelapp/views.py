from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
import pyrebase 

from django.http import HttpResponse

from .models import fcm_info, angeltable

from pyfcm import FCMNotification

# Create your views here.

config = {
    "apiKey": "AIzaSyCUJgLF1b8HoRouY40zzb4HxL13tQGjlSo",
    "authDomain": "angel-5ac50.firebaseapp.com",
    "databaseURL": "https://angel-5ac50.firebaseio.com",
    "projectId": "angel-5ac50",
    "storageBucket": "angel-5ac50.appspot.com",
    "messagingSenderId": "783783522765"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

class IndexView(TemplateView):
    template_name = 'base.html'
    #free_user = dict(db.child("FREE_USER").get().val())
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASE INJECTION!'
        return context


class List_user_page(ListView):
    model = angeltable
    template_name = 'angelapp/list_seekers_page.html'


class detailView(DetailView):
    context_object_name = 'details'
    model = angeltable
    template_name = 'angelapp/seekers_details.html'

# class ListUsers(TemplateView):
#     template_name = 'list_freespirits.html'
 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context = 
#         return context
        

def homePageView(request):
    prize = "<h1>Hello There</h1>"
    tokens = fcm_info.objects.all()
    for token in tokens:
        prize += token.fcm_token
        prize += '<br>'
    return HttpResponse(prize)


def fcm_insert(request):
    token = request.GET.get("fcm_token", '')
    a = fcm_info(fcm_token=token)
    a.save()
    return HttpResponse(token)

#the method which sends the notification


def send_notifications(request, reg_id):
    path_to_fcm = "https://angel-5ac50.firebaseio.com"
    server_key = 'AIzaSyA9l1_zDczB2Z1JkfmupsZ6gMljHhVKmnE'
    # quick and dirty way to get that ONE fcmId from table
    #reg_id = fcm_info.objects.all()[0].fcm_token
    message_title = "Zeo Learn"
    message_body = "Hi john, Zeo learn Rocks!"
    result = FCMNotification(api_key=server_key).notify_single_device(
        registration_id=reg_id, message_title=message_title, message_body=message_body)
    return HttpResponse(result)
