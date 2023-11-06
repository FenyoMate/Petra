"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
import PetraBot
from PetraBot import views
from accounts import views as account_views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^chat/(?P<pk>\d+)/$', views.chat, name='chat'),
    re_path(r'^chat/$', views.chat, name='chat'),
    re_path(r'^user/$', views.user, name='user'),
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^signup/$', account_views.signup, name='signup'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^uc/$', views.uc, name='underconstr')
]
