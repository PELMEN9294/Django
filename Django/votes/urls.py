from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns = [
    url(r'^(?P<question_text>[0-9]+)/votes/$', views.votes, name='votes'),
]

urlpatterns = [
    url(r'^(?P<question_text>[0-9]+)/$', views.detail, name='detail'),
]

urlpatterns = [
    url(r'^(?P<question_text>[0-9]+)/results/$', views.results, name='results'),
]