from methodism import custom_response, error_params_unfilled
from materio.methods.direktor.home_page import direc_inspection
from materio.models.ombor import Storage


def add_ombor(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    all_info = next((field for field in [
        "name", "location", "product_num", "money_type", "employee_num"
    ] if field not in params), '')

    if all_info:
        return custom_response(status=False, message=error_params_unfilled(all_info))

    Storage.objects.get_or_create(
        name=params['name'],
        location=params['location'],
        product_num=params['product_num'],
        money_type=params['money_type'],
        employee_num=params['employee_num']
    )

    return custom_response(status=True, message={"Succes": "Ombor qo'shildi"})


def get_ombor(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.storges_format() for x in Storage.objects.all()]
    }


def update_ombor(request, params):
    error = next((field for field in [
        "name", "location", "product_num", "money_type", "employee_num"
    ] if field not in params), '')
    if error:
        return custom_response(status=False, message=error_params_unfilled(error))

    ombor = Storage.objects.get(name=params['name'])

    for field in ['name', 'location', 'product_num', 'money_type', 'employee_num']:
        setattr(ombor, field, params.get(field, getattr(ombor, field)))

    ombor.save()
    return custom_response(True, message={"Succes": "Malumot qayta yuklandi"})


# next funksiyasi, berilgan bir ro'yxatdan birinchi elementni qaytaradi for bo'gani uchun 1tasi bo'ladi har doim
# setattr """obyektda""" o'zgartirishni istagan atribut nomla yangi qiymatlar bilan birga beradi
# getattr esa o'qishni istagan atribut nomini oziga ob ketadi va uni qiymat bilan qaytariadi
# karochi setattr o'sha kirgizayotgan narsamiz bilan kirgizishimiz kerak bo'lgani teng qilib ketadi
# karochi gett=attr shunchaki ularni ko'rish uchun ishlatiladi huddi oddiy get bilan birhil


def delete_ombor(request, params):
    try:
        ombor = Storage.objects.get(name=params['name'])
        ombor.delete()
        return custom_response(status=True, message="Succes")
    except Storage.DoesNotExist:
        return custom_response(status=False, message={"Error": "Bunday ombor topilmadi"})
