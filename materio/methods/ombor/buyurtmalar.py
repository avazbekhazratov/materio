from methodism import custom_response, error_params_unfilled, MESSAGE
from materio.models import Ombor_buyurtma, Storage, Storage_order
from materio.methods.direktor.home_page import direc_inspection


def omborga_buyurtma(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    not_params = next((field for field in ["ombor", "order_status", "order"] if field not in params), '')

    if not_params:
        return custom_response(status=False, message=error_params_unfilled(not_params))

    ombor_name = params['ombor']
    ombor = Storage.objects.get(name=ombor_name)
    order_status = params['order_status']
    order_name = params['order']

    try:
        order = Storage_order.objects.get(name=order_name)

    except Storage_order.DoesNotExist:
        return custom_response(status=False, message="Order does not exist")

    created = Ombor_buyurtma.objects.get_or_create(ombor=ombor, order_status=order_status, order=order)
    if not created:
        return {"Error"}

    return custom_response(status=True, message={"Success": "Buyurtma qilindi"})


def get_storage_order(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.storage_order_format() for x in Storage_order.objects.all()]
    }


def delete_storge_order(request, params):

    ombor = Ombor_buyurtma.objects.get(id=params['id'])
    if not ombor:
        return custom_response(status=False, message={"Error": "Bunday ombor topilmadi"})
    ombor.delete()
    return custom_response(status=True, message="Succes")
