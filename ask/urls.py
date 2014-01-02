from ask.views import QuestList
from ask.views import QuestDetailView

from ask import views
from ask import ajax_view
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', QuestList.as_view(), name='list'),
    url(r'^ajax/test/$', views.get_ajax_add_quest, name='contact'),
    url(r'^ajax/login/$', views.get_ajax_login, name='login'),
    url(r'^ajax/register/$', views.get_ajax_reg, name='register'),
    url(r'^ajax/logout/$', views.get_ajax_logout, name='register'),
    url(r'^quest(?P<pk>\d+)/$', QuestDetailView.as_view(), name='detail'),
    url(r'^page(?P<page>\d+)/$', QuestList.as_view(), name='detail'),
    url(r'^user(?P<id>\d+)/$', views.user_info, name='detail'),

)
