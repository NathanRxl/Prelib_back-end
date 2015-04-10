from django.conf.urls import patterns, url
from report import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<station_id>\d{5})/(?P<available_bikes>\d{1,2})/(?P<broken_bikes>\d{1,2})/$', views.add_report, name='add_report'),
    url(r'^(?P<station_id>\d{5})/$', views.ask_latest_reports, name='ask_latest_reports'),
)