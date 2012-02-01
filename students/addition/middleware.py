#-*- coding: utf-8 -*-
import time
from django.template import Template, Context
from django.db import connection

class StatMiddleware:
    def process_request(self, request):
        self.start_time = time.time()
        return None

    def process_response(self, request, response):
        qr_delta = time.time() - self.start_time
        qr_count = len(connection.queries)
        if request.META['CONTENT_TYPE'] in ('text/html', 'text/plain'):
            content = "<hr>Время выполнения: %s сек. <br>Кол-во запросов: %s " % (qr_delta, qr_count)
            pos = response.content.find("</body>")
            response.content = response.content[:pos] + content + response.content[pos:]
        return response