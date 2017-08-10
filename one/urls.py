"""one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from myapp import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r"^contact/$",TemplateView.as_view(template_name="contact.html"), name='contact'),
    url(r"^bo/$",views.bo_view, name='bo'),
    url(r"^bo/(?P<name>\w+)/$",views.item_detail_bo,name='bo_item_detail'),
    url(r"^bo/(?P<name>\w+)/edit/$",views.edit_detail_bo,name='edit_detail_bo'),
    url(r"^bo/(?P<name>\w+)/showlog/$",views.show_log_bo,name='show_log_bo'),
    # url(r"^(?P<id>\w+)$", views.list_cat_uatvn1, name='list_cat_uatvn1.html'),
    url(r"^ntd/$",views.ntd_view, name='ntd'),
    url(r"^ntd/(?P<name>\w+)/$",views.item_detail_ntd,name='ntd_item_detail'),
    url(r"^ntd/(?P<name>\w+)/edit/$",views.edit_detail_ntd,name='edit_detail_ntd'),
    url(r"^social/$", views.social_view, name='social'),
    url(r"^social/(?P<name>\w+)/$", views.item_detail_social, name='social_item_detail'),
    url(r"^social/(?P<name>\w+)/edit/$", views.edit_detail_social, name='edit_detail_social'),
    url(r"^batch/$", views.batch_view, name='batch'),
    url(r"^batch/(?P<name>\w+)/$", views.item_detail_batch, name='batch_item_detail'),
    url(r"^batch/(?P<name>\w+)/edit/$", views.edit_detail_batch, name='edit_detail_batch'),
    url(r"^activemq/$", views.activemq_view, name='activemq'),
    url(r"^activemq/(?P<name>\w+)/$", views.item_detail_activemq, name='activemq_item_detail'),
    url(r"^activemq/(?P<name>\w+)/edit/$", views.edit_detail_activemq, name='edit_detail_activemq'),
    url(r"^memcache/$", views.activemq_view, name='memcache'),
    url(r"^memcache/(?P<name>\w+)/$", views.item_detail_activemq, name='memcache_item_detail'),
    url(r"^memcache/(?P<name>\w+)/edit/$", views.edit_detail_activemq, name='edit_detail_memcache'),

]
