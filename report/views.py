from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from report.models import Report
from stationdict import stations

def index(request):
    latest_reports = Report.objects.order_by('-report_date')[:4]
    output = " ".join(str(report) for report in latest_reports)
    return HttpResponse(output)

def add_report(request, station_id, available_bikes, broken_bikes):
    if available_bikes >= broken_bikes:
        if station_id in stations:
            new_report = Report(report_date=timezone.now(),
                                station_id=station_id,
                                broken_bikes=broken_bikes,
                                available_bikes=available_bikes)
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

def ask_latest_reports(request, station_id):
    if station_id in stations:
        if len(Report.objects.filter(station_id=station_id).order_by('-report_date')) >= 1:
            last_report = Report.objects.filter(station_id=station_id).order_by('-report_date')[0]
            return HttpResponse("%s" % last_report.broken_bikes)
        else:
            return HttpResponse("0")
    else:
        return HttpResponse("Sorry, but #%s is not a valid station id."
                                    % station_id)