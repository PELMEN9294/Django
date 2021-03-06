from django.conf.urls import url
from .import views

app_name = 'votes'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/votes/$', views.votes, name='votes'),
    url(r'^(?P<question_id>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results')
]