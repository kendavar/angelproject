from django.urls import path
from django.views.generic.base import TemplateView
from . import views
app_name = 'angelapp'

urlpatterns = [
    path(r'', views.List_user_page.as_view(), name='home'),
    path(r'<int:pk>', views.detailView.as_view(), name='detail'),
    path(r'send/<str:reg_id>/<str:firebase_id>/', views.send_notifications, name='send'),
    path(r'createquote/',views.create_quote,name="create_quote"),
    path(r'quotes/', views.List_quotes.as_view(), name='quote'),
    path(r'updateSeeker/',views.update_seekers,name="updateSeeker"),
    path(r'terms/',views.terms.as_view(),name="terms")
  
]

