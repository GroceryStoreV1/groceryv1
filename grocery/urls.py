from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vegetables/$', views.vegetables, name='vegetables'),
    url(r'^products/$', views.products, name='products'),
    url(r'^drinks/$', views.drinks, name='drinks'),
    url(r'^pet/$', views.pet, name='pet'),
    url(r'^bread/$', views.bread, name='bread'),
    url(r'^household/$', views.household, name='household'),
    url(r'^kitchen/$', views.kitchen, name='kitchen'),
    url(r'^short-codes/$', views.kitchen, name='shortCodes'),
    url(r'^frozen/$', views.kitchen, name='frozen'),
  ]