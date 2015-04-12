from django.db import models
from django.utils import timezone
from datetime import datetime

class Report(models.Model):
    report_date = models.DateTimeField('Date of report')
    station_id = models.IntegerField('Station id')
<<<<<<< HEAD
    broken_bikes = models.IntegerField('Number of broken bikes')

    def __str__(self):
        columns = [datetime.strftime(self.report_date, "%d\%m\%Y %X"), str(self.station_id), str(self.broken_bikes)]
        return "(" + ", ".join(columns) + ")"
    
=======
    available_bikes = models.IntegerField('Number of available bikes')
    broken_bikes = models.IntegerField('Number of broken bikes')

    def __str__(self):
        columns = [datetime.strftime(self.report_date, "%d\%m\%Y %X"),
                   str(self.station_id),
                   str(self.available_bikes),
                   str(self.broken_bikes)]
        return "(" + ", ".join(columns) + ")"
>>>>>>> ba40893cfc03f3c84497840daff9d73f4c62a4e5
