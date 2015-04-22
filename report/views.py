from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from report.models import Report
from stationdict import stations
from datetime import datetime
import json


def index(request):
    latest_reports = Report.objects.order_by('-report_date')[:4]
    output = " ".join(str(report) for report in latest_reports)
    return HttpResponse(output)


def add_report(request, station_id, available_bikes, broken_bikes):
    if int(available_bikes) >= int(broken_bikes):
        if station_id in stations:
            new_report = Report(report_date=timezone.now(),
                                station_id=station_id,
                                available_bikes=available_bikes,
                                broken_bikes=broken_bikes)
            new_report.save()
            if(int(broken_bikes)>=2):
                return HttpResponse("Thanks for reporting broken bikes. We note that at the moment, %s bikes out of %s are broken at station #%s."
                                    % (broken_bikes, available_bikes, station_id))
            elif(int(broken_bikes)==1):
                return HttpResponse("Thanks for reporting broken bikes. We note that at the moment, 1 bike out of %s is broken at station #%s."
                                    % (available_bikes, station_id))
            else:
                return HttpResponse("Thanks for reporting broken bikes. We note that at the moment, no bikes are broken at station #%s."
                                    % station_id)
        else:
            return HttpResponse("Sorry, but #%s is not a valid station id."
                                    % station_id)
    else:
        return HttpResponse("Sorry, but it is absurd that %s bikes are broken out of %s at station #%s."
                                    % (broken_bikes, available_bikes, station_id))

def see_last_report(request, station_id):
    ''' Returns a dictionnary with data about the last report in JSON'''
    if station_id in stations:
        latest_reports = Report.objects.filter(station_id=station_id).order_by('-report_date')
        if len(latest_reports) >= 1:
            last_report = latest_reports[0]

            report_date = last_report.report_date
            broken_bikes = last_report.broken_bikes
            available_bikes = last_report.available_bikes
            return_dict = {
                            'report_date':'{}'.format(datetime.strftime(report_date, "%d\%m\%Y %X")),
                            'broken_bikes':'{}'.format(broken_bikes),
                            'available_bikes':'{}'.format(available_bikes),
                            'station_id':'{}'.format(station_id)
                          }
            return HttpResponse(json.dumps(return_dict))
        else:
            return HttpResponse("There is no report yet for this station.")
    else:
        return HttpResponse("Sorry, but #%s is not a valid station id."
                            % station_id)