from django.shortcuts import render
from django.http import HttpResponse, Http404

import datetime
# Create your views here.
def time(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    if 0 <= offset < 100:
        dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
        html = "<html><body> Across %s will be %s. </body></html>" % (offset, dt)
    else:
        raise Http404()
    return HttpResponse(html)
