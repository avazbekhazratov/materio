from methodism import custom_response, MESSAGE

from materio.models import User


def direc_inspection(request):
    if request.user.user_type != 1:
        return custom_response(False, message=MESSAGE['PermissionDenied'])
    return custom_response(True)


def magazin_inspection(request):
    if request.user.user_type != 3:
        return custom_response(False, message=MESSAGE['PermissionDenied'])
    return custom_response(True)


def user_deletes(request, params):
    a = User.objects.get(username=params['name'])
    a.delete()
    return True
