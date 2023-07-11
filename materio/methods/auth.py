import datetime, re, random, string, uuid
from methodism import custom_response, error_params_unfilled, MESSAGE, error_msg_unfilled, generate_key, code_decoder, \
    exception_data
from rest_framework.authtoken.models import Token
from materio.models import User
from base.server import check_email_in_db, check_token_in_db, check_user_in_token_db, update_token
from base.sen_email import send_email
from materio.models.auth import OTP, user_types


def regis(requests, params):
    try:

        nott = 'phone' if 'phone' not in params else 'password' if 'password' not in params else 'token' if 'token' not in params else 'username' if 'username' not in params else ''
        if nott:
            return custom_response(False, message=error_params_unfilled(nott))

        otp = OTP.objects.filter(key=params['token']).first()

        if not otp:
            return custom_response(False, {"Error": "Неверный токен !"})

        if otp.is_conf:
            return custom_response(False, {"Error": "Устаревший токен !"})

        user = User.objects.filter(email=otp.email).first()

        if user:
            return custom_response(False, {"Error": "Этот эмайл ранее был зарегистрирован"})
        if len(params['password']) < 8 or params['password'].isalnum() or " " in params['password']:
            return custom_response(False, {
                "Error": "Длина пароля должно быть не меннее 8 символов и больше 2х занков без пробелов !"})

        user_data = {
            "password": params['password'],
            "username": params['username'],
            "phone": params.get('phone', ''),
            "email": OTP.objects.filter(email=params.get('email', otp.email))
        }

        if params.get('key', None):
            user_data.update({
                "is_staff": True,
                "is_superuser": True,
                "type": user_types(params['key'])
            })

        userr = User.objects.create_user(**user_data)
        token = Token.objects.create(user=userr)
        return custom_response(False, {
            "Success": "Ваш аккаунт успешно создан",
            "Ваш секретный ключ": token.key
        })
    except Exception as e:
        return exception_data(e)


def login(request, params):
    not_data = 'phone' if 'phone' not in params else 'password' if 'password' not in params else ''
    if not_data:
        return custom_response(False, message=error_params_unfilled(not_data))

    user = User.objects.filter(phone=params['phone']).first()
    if not user:
        return custom_response(False, message=MESSAGE['UserNotFound'])

    if not user.check_password(params['password']):
        return custom_response(True, message=MESSAGE['UserPasswordError'])

    token = Token.objects.get_or_create(user=user)
    return custom_response(True, data={"succes": token[0].key})


def logout(request, params):
    token = Token.objects.filter(user=request.user).first()
    if token:
        token.delete()
    return custom_response(True, message=MESSAGE['LogedOut'])


def user_update(request, params):
    nott = 'password' if 'password' not in params else 'new_password' if 'new_password' not in params else ''
    if nott:
        custom_response(True, error_msg_unfilled(nott))
    if not request.user.check_password(params['password']):
        return custom_response(True, message={"Error": "Parol noto'g'ri"})

    if request.user.check_password(params['new_password']):
        return custom_response(True, message={"Error": "Parol eskisi bilan teng bo'lishi kerek emas"})

    if len(str(params['new_password'])) < 6 or params['new_password'].isalnum() or ' ' in params['new_password']:
        return custom_response(True, message=MESSAGE['ParamsNotFull'])
    request.user.set_password(params['new_password'])
    request.user.save()

    user = User.objects.filter(phone=params['phone']).first()

    if type(params['phone']) is not int and len(str(params['phone'])) < 12:
        error_msg = f"'{params['phone']}' phone 👈 12ta raqam"
        return custom_response(True, message=error_params_unfilled(error_msg))
    if user and user.id != request.user.id:
        return custom_response(True, message={"Error": "Bunaqa user band qilingan"})

    request.user.phone = params.get('phone', request.user.phone)
    request.user.username = params.get('username', request.user.phone)
    # request.user.email = params.get('email', request.user.email)
    request.user.last_name = params.get('last_name', request.user.last_name)
    request.user.save()
    return custom_response(True, message={"Succes": "User update qilindi"})


def user_delete(request, params):
    request.user.delete()
    return custom_response(True, message=MESSAGE['UserSuccessDeleted'])


# def StepOne(request, params):
#     not_data = 'phone' if 'phone' not in params else ''
# 
#     if not_data:
#         return custom_response(True, message=error_msg_unfilled(not_data))
# 
#     if 'phone' in params:
#         if type(params['phone']) is not int or len(str(params['phone'])) < 12:
#             error_msg = f"'{params['phone']}' phone 👈 12ta raqam"
#             return custom_response(True, message=error_params_unfilled(error_msg))
# 
#     code = random.randint(100000, 999999)
#     sms = send_sms(otp=code, phone=params['phone'])
#     if sms['status'] != 'waiting':
#         return custom_response(True, message=error_params_unfilled(sms))
# 
#     shifr = uuid.uuid4().__str__() + "$" + str(code) + "$" + generate_key(20)
# 
#     shifr = code_decoder(shifr, l=5)
# 
#     # letters = string.ascii_letters
#     # digits = string.digits
# 
#     # for_help = digits + letters + digits
#     # code = ''.join(for_help[random.randint(0, len(for_help)-1)] for i in range(10))
# 
#     otp = OTP.objects.create(key=shifr, phone=params['phone'])
# 
#     return custom_response(True, data={
#         "code": code,
#         'shifr': otp.key
#     })

def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


def StepOne(request, params):
    if 'email' not in params:
        return custom_response(False, message={"Error": "The data is incomplete"})

    check_email(params['email'])

    user = check_email_in_db(params['email'])
    if user:
        return custom_response(False, message={"Error": "Such a user exists"})

    code = random.randint(100000, 999999)
    # send_email(OTP=code, email=params['email'])
    shifr = uuid.uuid4().__str__() + "$" + str(code) + "$" + generate_key(20)
    shifr = code_decoder(shifr, l=5)

    otp = OTP.objects.create(key=shifr, email=params['email'])

    return custom_response(True, message={
        "otp": code,
        "token": otp.key
    })


# def StepTwo(request, params):
#     not_base = 'otp' if 'otp' not in params else '' or 'token' if 'token' not in params else ''
#     if not_base:
#         return custom_response(True, error_params_unfilled(not_base))
#
#     token = OTP.objects.filter(key=params['token']).first()
#
#     if not token:
#         return custom_response(True, message=('token topilmadi'))
#
#     if token.is_expire:
#         return custom_response(True, message=('token eskirdi'))
#
#     if token.is_conf:
#         token.is_conf = True
#         token.save()
#
#         return custom_response(True, message=MESSAGE['TokenUnUsable'])
#
#     now = datetime.datetime.now(datetime.timezone.utc)
#
#     if (now - token.create).total_seconds() > 18000:
#         token.is_expire = True
#         token.save()
#
#         return custom_response(False, message=MESSAGE['TokenUnUsable'])
#
#     code = code_decoder(token.key, decode=True, l=5).split("$")[1]
#     if code != str(params['otp']):
#         token.tires += 1
#         token.save()
#         return custom_response(True, message=MESSAGE['TokenUnUsable'])
#
#     token.is_conf = True
#     user = User.objects.filter(phone=token.phone).first()
#
#     return custom_response(True, message={"is_registered": user is not None})

def StepTwo(request, params):
    nott = 'otp' if 'otp' not in params else 'token' if 'token' not in params else ''
    if nott:
        return custom_response(False, message=error_params_unfilled(nott))

    token = check_token_in_db(params['token'])
    token_dete = OTP.objects.filter(key=params['token']).first()

    if not token:
        return custom_response(False, message=MESSAGE['AuthToken'])

    if token['is_conf']:
        return custom_response(False, message=MESSAGE["TokenUnUsable"])

    if token['is_expire']:
        return custom_response(False, message=MESSAGE['TokenUnUsable'])

    now = datetime.datetime.now(datetime.timezone.utc)

    if (now - token_dete.created).total_seconds() >= 1800:
        token['is_expire'] = True
        update_token(token)
        return custom_response(False, message={"Error": "Tokenga ajratilgan vaqt tugadi"})

    code = code_decoder(token['key'], decode=True, l=5).split('$')[1]

    if str(params['otp']) != code:
        token['tries'] += 1
        update_token(token)
        return custom_response(True, message=MESSAGE['PasswordError'])

    token['is_conf'] = True
    update_token(token)

    return custom_response(True, message={
        "Succes": "Worked",
        'otp': code
    })
