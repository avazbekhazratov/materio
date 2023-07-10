from methodism import custom_response, MESSAGE


def direc_inspection(request):
    if request.user.user_type != 1:
        return custom_response(False, message=MESSAGE['PermissionDenied'])
    return custom_response(True)


def magazin_inspection(request):
    if request.user.user_type != 3:
        return custom_response(False, message=MESSAGE['PermissionDenied'])
    return custom_response(True)

#
# ombor qo'shish' update qilish chetan qabul qilinan mahsulotlar ro'yxati omborga buyurtma' ombor yoki do'konga '
# shularni ertaga boshlanishiga yozishim kereak keyin filter qilishim kerak do'konni chatgptida filtr' \
#                                                                             ' qilingan kodlari bor'
# keyin do'kon ro'yhati va allanbalo narsalani qilishim kerak tzda direktr sahifasida do'konlar sahifasi deb yozilgani \'
# hammasini
# bulani ichida do'
# bulani ichida do'
#
# ertaga Ustozdan kassa(tushm, chiqim)->> valyuta tizimini keyin savdo modelari va funksiyasi bo'yicha so'rashim kere
