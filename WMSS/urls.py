"""WMSS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from crawling import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homePageView, name='homePageView'),
    url(r'^crawling/$', views.crawlingView, name='crawlingView'),
    url(r'^crawling/hasil_keyword/', views.hasil, name='hasil'),
    url(r'^crawling/open_url/', views.open_url, name='open_url'),
    url(r'^crawling/buka_url/$', views.buka_url, name='buka_url'),
    url(r'^crawling/upload_file/$', views.upload_file, name='upload_file')
]
