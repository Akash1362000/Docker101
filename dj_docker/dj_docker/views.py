import datetime
from django.http import HttpResponse


def Home(request):
    now = datetime.datetime.now()
    html = (
        """<html>
        <h1>Hello from Docker 101 container!</h1>
        <body>Current date and time is -  %s.</body>
        </html>"""
        % now
    )
    return HttpResponse(html)
