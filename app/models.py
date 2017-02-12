from django.db import models


class Report(models.Model):
    document_uri = models.URLField("document-uri", blank=True)
    referrer = models.CharField("referrer", max_length=250, blank=True)
    blocked_uri = models.URLField("blocked-uri", blank=True)
    effective_directive = models.CharField("effectiveDirective", blank=True, max_length=250)
    violated_directive = models.CharField("violatedDirective", max_length=250, blank=True)
    original_policy = models.CharField("originalPolicy", max_length=250, blank=True)
    disposition = models.CharField("disposition", max_length=250, blank=True)
    source_file = models.CharField("sourceFile", max_length=250, blank=True)
    status_code = models.CharField("statusCode", max_length=250, blank=True)
    line_number = models.CharField("lineNumber", max_length=250, blank=True)
    column_number = models.CharField("columnNumber", max_length=250, blank=True)

    def __str__(self):
        return self.document_uri
