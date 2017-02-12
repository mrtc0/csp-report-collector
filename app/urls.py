from django.conf.urls import url
from .views import create_report


urlpatterns = [
    url(r'^report/$', create_report, name='create_report'),
]
