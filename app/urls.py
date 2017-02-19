from django.conf.urls import url
from .views import create_report, show_index


urlpatterns = [
    url(r'^report/$', create_report, name='create_report'),
    url(r'^$', show_index, name='show_index')
]
