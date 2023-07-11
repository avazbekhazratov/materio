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
    try:
        ombor = User.objects.get(id=params['id'])
        ombor.delete()
        return custom_response(status=True, message="Succes")
    except User.DoesNotExist:
        return custom_response(status=False, message={"Error": "gg"})


def get_user(request, params):
    return {
        "result": [x.formats_users() for x in User.objects.all()]
    }
