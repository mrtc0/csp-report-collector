# from django.shortcuts import render
from django.http.response import JsonResponse
import json
from .models import Report


def create_report(request):
    reports = json.loads(request.body.decode("utf-8"))["csp-report"]

    Report.objects.create(
        document_uri=reports.get("document-uri", ""),
        referrer=reports.get("referrer", ""),
        blocked_uri=reports.get("blcoked-uri", ""),
        effective_directive=reports.get("effective-directive", ""),
        violated_directive=reports.get("violated-directive", ""),
        original_policy=reports.get("original-policy", ""),
        disposition=reports.get("disposition", ""),
        source_file=reports.get("source-file", ""),
        status_code=reports.get("status-code", ""),
        line_number=reports.get("line-number", ""),
    )

    return JsonResponse({"status": "OK"})
