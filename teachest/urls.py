from django.conf.urls import patterns, url
from teagraphs import views

urlpatterns = patterns('',
            #url(r'^$', views.index, name='index'),
            url(r'^made$', views.made, name='made'),
            url(r'^addtea$', views.addtea, name='addtea'),
            url(r'^teamakers$', views.teamakers, name='teamakers'),
            url(r'^teadaily$', views.teadaily, name='teadaily'),
            url(r'^teasprint$', views.teasprint, name='teasprint'),
            url(r'^teatypes$', views.teatypes, name='teatypes'),
            )
