from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
import PetraBot
from PetraBot import views
from accounts import views as account_views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^chat/(?P<pk>\d+)/$', views.chat, name='chat'),
    re_path(r'^chat/$', views.new_chat, name='new_chat'),
    re_path(r'^setup/$', account_views.profileSetup, name='setup'),
    re_path(r'^context/$', account_views.context, name='context'),
    re_path(r'^permissions/$', account_views.permissions, name='permissions'),
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^signup/$', account_views.signup, name='signup'),
    re_path(r'^logout/$', account_views.logout, name='logout'),
    re_path(r'^$', account_views.login, name='login'),
    re_path(r'^accounts/login/$', account_views.login, name='login'),
    re_path(r'^uc/$', views.uc, name='underconstr')
]
