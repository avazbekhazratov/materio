from methodism import custom_response, MESSAGE
from materio.models import Maxsulot, Storage, User
from materio.models.savdo import savdo_oynasi
from materio.models import Client
from materio.methods.direktor.home_page import magazin_inspection


def savdo_ooynasi(request, params):
    result = magazin_inspection(request)
    if not result['status']:
        return result

    if not result['status']:
        return result

    return {
        "result": [x.x_format() for x in savdo_oynasi.objects.all()]
    }


def add_savdo(request, params):
    result = magazin_inspection(request)
    if not result['status']:
        return result

    data = {
        'name_prod': params['name_prod'],
        'color_prod': params['color_prod'],
        'size_prod': params['size_prod'],
        'number_prod': params['number_prod'],
        'clent_bolsa': params['clent_bolsa'],
        'money_prod': params['money_prod'],
        'valyuta': params['valyuta'],
    }


def maxsulotlar_onyasi(request, params):
    result = magazin_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.product_format() for x in Maxsulot.objects.all()]
    }


def clent_oynasi(request, params):
    result = magazin_inspection(request)
    if not result['status']:
        return result

    return {
        "result": [x.clent_format() for x in Client.objects.all()]
    }


def buyurtma_oynasi(request, params):
    result = magazin_inspection(request)
    if not result['status']:
        return result

    if request.user.is_anonymous:
        return custom_response(status=False, message={"error"})


    if "name" not in params or "soni" not in params or "user_id" not in params:
        return custom_response(False, message="Params toliq emas")

    ombor = Storage.objects.filter(id=params["ombor_id"]).first()
    product = Maxsulot.objects.filter(product_name=params["name"]).first()
    if not product:
        return custom_response(False, message="Bunday mahsulot topilmadi")
    if not ombor:
        return custom_response(False, message={"bunday ID lik ombor yoq"})

    if ombor.product_num < params["soni"]:
        return custom_response(False, message="Mahsulot yetarli emas")

    a = User.objects.get(username=params['user_id'])
    if not a:
        return custom_response(status=False, message={"bunday user yo'q"})

    savdo_oynasi.objects.get_or_create(product=product, clent_bolsa=a, sotish_narxi=params['narx'], valyuta=params['valyuta'])

    return {
        "succes"
    }
