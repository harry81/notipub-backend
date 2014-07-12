# encoding: utf-8
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, render_to_response
import json
from django.template import RequestContext

from dowant.lib.logs import logs as logging
logger = logging.get_logger(__name__)


def home(request,
         template="notipub_message/index.html"):
    context = {}
    return render_to_response(template,
                                context, context_instance=RequestContext(request))

def register_token(request):
    msg =u'성공입니다.'
    response = json.dumps([('success', msg)])
    logger.error(response)
    return HttpResponse(response)

