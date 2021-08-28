from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Pet

def test(request):
    # data = json.loads(request.body)
    # is_mobile = data.get('isMobile')

    response = JsonResponse({'ok': True})

    # # check if user already has session
    # if request.session:
    #     # TODO: decide what to do if session already exists.
    #     #  delete session?
    #     request.session.endTime = timezone.now()
    #
    # session = SessionService.create_new_session()
    # session.ip = SessionService.get_client_ip(request)
    # session.isMobile = is_mobile
    # session.save()
    # # store session id as cookie on the client
    # response.set_cookie('session_id', session.sessionId)

    return response

def pets(request):
    if request.method == 'GET':
        pets = Pet.objects.filter()
        data = serializers.serialize('json', list(pets))
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        return JsonResponse({'ok': True}, safe=False)
