from django.contrib import admin
from report.models import Report

class ReportAdmin(admin.ModelAdmin):
    fieldsets = [
<<<<<<< HEAD
        ('Report information', {'fields': ['report_date', 'station_id', 'broken_bikes']}),
        ]
    list_display = ('report_date', 'station_id', 'broken_bikes')
=======
        ('Report information', {'fields': ['report_date', 'station_id', 'available_bikes', 'broken_bikes']}),
        ]
    list_display = ('report_date', 'station_id', 'available_bikes', 'broken_bikes')
>>>>>>> ba40893cfc03f3c84497840daff9d73f4c62a4e5
    list_filter = ['station_id']

admin.site.register(Report, ReportAdmin)
