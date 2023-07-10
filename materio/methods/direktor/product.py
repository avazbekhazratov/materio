from materio.methods.direktor.home_page import direc_inspection
from materio.models import Maxsulot
from methodism import custom_response, MESSAGE, error_params_unfilled


# def error(err, params):
#     error = next((field for field in [
#         f"{err}"
#     ] if field not in params), '')
#     if error:
#         return custom_response(status=False, message=error_params_unfilled(error))
# to'g'ri ishlatomadim


def get_product(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.prod_format() for x in Maxsulot.objects.all()]
    }


def add_product(request, params):
    result = direc_inspection(request)
    if not result['status']:
        return result

    all_info = next((field for field in [
        "product_name", "size", "color", "joyi", "soni", "product_price",
        "product_price_type", "entry_price", "entry_price_type"
    ] if field not in params), '')

    if all_info:
        return custom_response(status=False, message=error_params_unfilled(all_info))

    # if Maxsulot.objects.get(product_name=params['product_name']):
    #     return custom_response(status=False, message={"bunday maxsulot mavjud"})
    # shuyerda get funksiyasi to'liq ishlagani yo'q oldin yaratilmagan bo'lsa error beryapti yaratilgan bo'lsa to'g'ri ishlayapti
    Maxsulot.objects.get_or_create(
        product_name=params['product_name'],
        size=params['size'],
        color=params['color'],
        joyi=params['joyi'],
        soni=params['soni'],
        product_price=params['product_price'],
        product_price_type=params['product_price_type'],
        entry_price=params['entry_price'],
        entry_price_type=params['entry_price_type']
    )
    return custom_response(status=True, message={"Olma zakas qilindi tez orada yetib boradi"})


def update_product(request, params):
    error = next((field for field in [
        "product_name", "size", "color", "joyi", "soni", "product_price",
                 "product_price_type", "entry_price", "entry_price_type"
    ] if field not in params), '')
    if error:
        return custom_response(status=False, message=error_params_unfilled(error))

    try:
        prod = Maxsulot.objects.get(product_name=params['product_name'])
    except Maxsulot.DoesNotExist:
        return custom_response(status=False, message=MESSAGE['UserNotFound'])

    prod.size = params.get('size', prod.size)
    prod.color = params.get('color', prod.color)
    prod.joyi = params.get('joyi', prod.joyi)
    prod.soni = params.get('soni', prod.soni)
    prod.product_price = params.get('product_price', prod.product_price)
    prod.product_price_type = params.get('product_price_type', prod.product_price_type)
    prod.entry_price = params.get('entry_price', prod.entry_price)
    prod.entry_price_type = params.get('entry_price_type', prod.entry_price_type)
    prod.save()
    return custom_response(True, message={"Succes": "Malumot qayta yuklandi"})


def delete_product(request, params):
    try:
        ombor = Maxsulot.objects.get(product_name=params['product_name'])
        ombor.delete()
        return custom_response(status=True, message="Succes")
    except Maxsulot.DoesNotExist:
        return custom_response(status=False, message={"Error": "Bunday ombor topilmadi"})

