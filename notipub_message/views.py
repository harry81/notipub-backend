from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.
def home(request,
         template="notipub_message/index.html"):
    context = {}
    return render_to_response(template,
                                context, context_instance=RequestContext(request))
