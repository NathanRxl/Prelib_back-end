from django.test import TestCase

from django.test.client import Client
from django.utils import timezone
from report.models import Report
import report.views
from datetime import datetime
from django.http import HttpResponse

class ReportModelsTestCase(TestCase):
    def test_str_report(self):
        report18002 = Report(report_date=datetime(2012, 3, 3, 1, 30, 53, 567543),
                             station_id=18002,
                             available_bikes=5,
                             broken_bikes=3)
        self.assertTrue(str(report18002) == '(03\\03\\2012 01:30:53, 18002, 5, 3)')

class ReportViewsTestCase(TestCase):
    def test_add_report(self):
        report18002_valid = report.views.add_report(request=Client(),
                                                    station_id="18002",
                                                    available_bikes="10",
                                                    broken_bikes="6")
        print(report18002_valid)
        self.assertTrue(report18002_valid == HttpResponse("Thanks for reporting broken bikes. We note that at the moment, 6 bikes out of 10 are broken at station #18002."))

        report14600_unvaild = report.views.add_report(request=Client(),
                                                      station_id="14600",
                                                      available_bikes="10",
                                                      broken_bikes="6")
        self.assertTrue(report14600_unvalid == HttpResponse("Sorry, but #14600 is not a valid station id."))

        report18002_absurd = report.view.add_report(request=Client(),
                                                    station_id="18002",
                                                    available_bikes="4",
                                                    broken_bikes="10")
        self.assertTrue(report18002_absurd == HttpResponse("Sorry, but it is absurd that 10 bikes are broken out of 4 at station #18002."))

        report18002_valid_1 = report.views.add_report(request=Client(),
                                                    station_id=18002,
                                                    available_bikes=10,
                                                    broken_bikes=1)
        self.assertTrue(report18002_valid_1 == HttpResponse("Thanks for reporting broken bikes. We note that at the moment, 1 bike out of 10 is broken at station #18002."))

        report18002_valid_0 = report.views.add_report(request=Client(),
                                                    station_id=18002,
                                                    available_bikes=10,
                                                    broken_bikes=0)
        self.assertTrue(report18002_valid_0 == HttpResponse("Thanks for reporting broken bikes. We note that at the moment, no bikes are broken at station #18002."))

        self.assertTrue(len(Reports.objects.all()) == 3)
