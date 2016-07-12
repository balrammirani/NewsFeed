from django.conf.urls import url
from django.contrib import admin
from users.views import UserCreateAPIView,UserLoginAPIView

app_name = 'users'

urlpatterns = [
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),

]
