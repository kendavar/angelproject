from django.conf.urls import url

app_name = 'angelapp'

urlpatterns = [
    url(r'profile/$',views.profile,name="profile")
]