from django.shortcuts import render
from django.http import JsonResponse

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
