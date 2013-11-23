from ask.views import QuestList
from ask.views import QuestDetailView

from ask import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', QuestList.as_view(), name='list'),
    #url(r'^$', views.contact, name='contact'),
    url(r'^(?P<pk>\d+)/$', QuestDetailView.as_view(),name='detail'),

)
