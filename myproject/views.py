from django.shortcuts import render_to_response
from django.template import RequestContext


def main(request):
    return render_to_response('myproject/main.html',context_instance=RequestContext(request))
