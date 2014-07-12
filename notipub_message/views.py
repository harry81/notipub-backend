# encoding: utf-8
import json

from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template import RequestContext

from notipub_message.models import DeviceToken

from dowant.lib.logs import logs as logging
logger = logging.get_logger(__name__)


def home(request,
         template="notipub_message/index.html"):
    context = {}
    return render_to_response(template,
                                context, context_instance=RequestContext(request))

@csrf_exempt
def register_token(request):
    token = request.GET.get('token', None)
    uuid = request.GET.get('uuid', None)
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)

    dev = DeviceToken(token=token, uuid=uuid)
    #dev.save()

    data = {
        "result_code": 0,
        "message": u"서비스 가능 지역이 아닙니다.",
    }


    response = json.dumps(data)
    logger.error(response)
    return HttpResponse(response)

