from methodism import custom_response, MESSAGE, error_params_unfilled
from .home_page import direc_inspection
from materio.models.xodim import Employee


def add_xodim(request, params):
    if "name" not in params or "phone" not in params or "passport" not in params:
        return custom_response(False, message=MESSAGE['ParamsNotFull'])

    saves = Employee.objects.get_or_create(name=params['name'], phone=params['phone'], passport=params['passport'])[0]

    if not saves:
        return custom_response(status=False, message={"Error"})

    return {
        "usrra": saves.employee_format()
    }


def get_xodim(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.employee_format() for x in Employee.objects.all()]
    }


def update_xodim(request, params):
    error = next((field for field in ["name", "phone", "passport"] if field not in params), '')
    if error:
        return custom_response(status=False, message=error_params_unfilled(error))

    try:
        xodim = Employee.objects.get(passport=params['passport'])
    except Employee.DoesNotExist:
        return custom_response(status=False, message=MESSAGE['UserNotFound'])

    xodim.name = params.get('name', xodim.name)
    xodim.phone = params.get('phone', xodim.phone)
    xodim.passport = params.get('passport', xodim.passport)
    xodim.save()
    return custom_response(True, message={"Succes"})
