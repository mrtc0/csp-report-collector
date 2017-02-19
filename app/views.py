# from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import render
import json
from .models import Report
import re


def get_headers(request):
    regex = re.compile('^HTTP_')
    return dict((regex.sub('', header), value) for (header, value) in request.META.items() if header.startswith('HTTP_'))

def create_report(request):
    headers = json.dumps(get_headers(request))
    reports = json.loads(request.body.decode("utf-8"))["csp-report"]

    Report.objects.create(
        document_uri=reports.get("document-uri", ""),
        referrer=reports.get("referrer", ""),
        blocked_uri=reports.get("blocked-uri", ""),
        effective_directive=reports.get("effective-directive", ""),
        violated_directive=reports.get("violated-directive", ""),
        original_policy=reports.get("original-policy", ""),
        disposition=reports.get("disposition", ""),
        source_file=reports.get("source-file", ""),
        status_code=reports.get("status-code", ""),
        line_number=reports.get("line-number", ""),
        http_header=headers,
    )

    return JsonResponse({"status": "OK"})


def show_index(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'reports': reports})
