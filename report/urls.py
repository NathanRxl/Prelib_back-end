from django.conf.urls import patterns, url
from report import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
<<<<<<< HEAD
    url(r'^(?P<station_id>\d{5})/(?P<broken_bikes>\d{1,2})/$', views.add_report, name='add_report'),
    url(r'^(?P<station_id>\d{5})/$',views.see_last_report, name='see_last_report'),
)
=======
    url(r'^(?P<station_id>\d{5})/(?P<available_bikes>\d{1,2})/(?P<broken_bikes>\d{1,2})/$', views.add_report, name='add_report'),
    url(r'^(?P<station_id>\d{5})/$', views.ask_latest_reports, name='ask_latest_reports'),
)
>>>>>>> ba40893cfc03f3c84497840daff9d73f4c62a4e5
