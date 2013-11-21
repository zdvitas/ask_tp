from ask.views import QuestList
from ask import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    #url(r'^$', views.contact, name='contact'),
    url(r'^$', QuestList.as_view(), name='list'),

)
