from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^sismos$',views.sismos_list),
    url(r'^sismos/new/$', views.sismo_new, name='sismo_new'),
    url(r'^sismos/(?P<pk>[0-9]+)/edit/$', views.sismo_edit, name='sismo_edit'),
    url(r'^sismos/(?P<pk>\d+)/remove/$', views.sismo_remove, name='sismo_remove'),
    url(r'^sismos/(?P<pk>\d+)/detail/$', views.sismo_detail, name='sismo_detail'),
    url(r'^sismos/grafico/$', views.grafico, name='grafico'),
]
