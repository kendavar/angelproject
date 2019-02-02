from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
import pyrebase 
from django.http import HttpResponse, HttpResponseRedirect
from .models import fcm_info, angeltable, quotes
from .forms import PostForm
from pyfcm import FCMNotification
from firebase_to_db import update_db

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

class List_quotes(ListView):
    model = quotes
    template_name = 'angelapp/quotes.html'


def create_quote(request):
    if request.method == 'POST' :
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            quote = form.cleaned_data['quote']
            data = {"quote": quote}               
            db.child("quotes").push(data)
            form.cleaned_data['firebase_id'] = list(dict(db.child("quotes").get().val()).keys())[-1]
            send_quotes(quote)
            form.save(commit=True)
            return HttpResponseRedirect('/')
    else:
        form = PostForm()

    return render(request, 'angelapp/create_quotes.html', {'form': form})

class detailView(DetailView):
    context_object_name = 'details'
    model = angeltable
    template_name = 'angelapp/seekers_details.html'

def send_notifications(request, reg_id,firebase_id):
    db.child("FREE_USER").child(firebase_id).update({"flag": 1})
    path_to_fcm = "https://fcm.googleapis.com"
    server_key = 'AIzaSyA9l1_zDczB2Z1JkfmupsZ6gMljHhVKmnE'
    message_title = "Chat Enabled"
    message_body = "Hello Friend:), Now you can ask your queries with one of our executives!"
    print(reg_id)
    result = FCMNotification(api_key=server_key).notify_single_device(
        registration_id=reg_id, message_title=message_title, message_body=message_body)
    return HttpResponse(result)

# def send_quotes(quote):
#     path_to_fcm = "https://fcm.googleapis.com"
#     server_key = 'AIzaSyA9l1_zDczB2Z1JkfmupsZ6gMljHhVKmnE'
#     list(dict(db.child("FREE_USER").get().val()).keys())
#     reg_id = [k["deviceToken"] for v, k in db.child("FREE_USER").get().val().items() if type(k) == dict]
#     message_title = "Quote of the day"
#     message_body = quote
#     print(reg_id)
#     result = FCMNotification(api_key=server_key).notify_single_device(
#         registration_id=reg_id, message_title=message_title, message_body=message_body)
#     return 

def update_seekers(request):
    update_db()
    return HttpResponseRedirect('/angelapp/')

