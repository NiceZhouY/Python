"""testone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import xadmin
from django.conf.urls import url
from captcha import views

from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

from users.views import LoginView, RegisterView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    re_path(r'^index\.html', TemplateView.as_view(template_name='index.html'), name='index'),
    re_path(r'^login\.html', LoginView.as_view(), name='LoginView'),
    re_path(r'^register\.html', RegisterView.as_view(), name='RegisterView'),
    re_path(r'^course-list\.html', TemplateView.as_view(template_name='course-list.html'), name='course-list'),
    re_path(r'^teachers-list\.html', TemplateView.as_view(template_name='teachers-list.html'), name='teachers-list'),
    re_path(r'^org-list\.html', TemplateView.as_view(template_name='org-list.html'), name='org-list'),
    re_path(r'^usercenter-info\.html', TemplateView.as_view(template_name='usercenter-info.html'), name='usercenter-info'),
    re_path(r'^course-detail\.html', TemplateView.as_view(template_name='course-detail.html'), name='course-detail'),
    re_path(r'^org-detail-homepage\.html', TemplateView.as_view(template_name='org-detail-homepage.html'), name='org-detail-homepage'),
    re_path(r'^org-detail-course\.html', TemplateView.as_view(template_name='org-detail-course.html'), name='org-detail-course'),
    re_path(r'^org-detail-desc\.html', TemplateView.as_view(template_name='org-detail-desc.html'),name='org-detail-desc'),
    re_path(r'^org-detail-teachers\.html', TemplateView.as_view(template_name='org-detail-teachers.html'), name='org-detail-teachers'),
    re_path(r'^usercenter-fav-course\.html', TemplateView.as_view(template_name='usercenter-fav-course.html'), name='usercenter-fav-course'),
    re_path(r'^usercenter-message\.html', TemplateView.as_view(template_name='usercenter-message.html'),name='usercenter-message'),
    re_path(r'^usercenter-mycourse\.html', TemplateView.as_view(template_name='usercenter-mycourse.html'), name='usercenter-mycourse'),

    re_path(r'image/(?P<key>\w+)/$', views.captcha_image, name='captcha-image', kwargs={'scale': 1}),
    re_path(r'image/(?P<key>\w+)@2/$', views.captcha_image, name='captcha-image-2x', kwargs={'scale': 2}),
    re_path(r'audio/(?P<key>\w+).wav$', views.captcha_audio, name='captcha-audio'),
    re_path(r'refresh/$', views.captcha_refresh, name='captcha-refresh'),
]
