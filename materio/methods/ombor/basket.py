from methodism import custom_response, error_params_unfilled

from materio.models import Basket, Maxsulot


def add_savat(request, params):
    if "product_id" not in params:
        return custom_response(False, message="Params to'liq emas")

    noot = Maxsulot.objects.filter(id=params["product_id"]).first()
    if not noot:
        return custom_response(False, message=error_params_unfilled(noot))
    basket = Basket.objects.get_or_create(product=noot, user=request.user)[0]
    basket.quent = params.get("product_num", basket.quent)
    basket.save()
    return custom_response(True, message="Savatga qo'shildi")


def get_savat(request, params):
    return {
        "result": [x.format() for x in Basket.objects.filter(user=request.user, status=True)]
    }


def del_savat(request, params):
    if "product_id" not in params:
        return custom_response(False, message="Params to'liq emas")
    savat = Basket.objects.filter(id=params["product_id"]).first()
    if not savat:
        return custom_response(False, message="Id topilmadi")

    savat.delete()
    return custom_response(True, message="Basket deleted")

