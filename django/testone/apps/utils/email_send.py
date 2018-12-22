# -*- coding: utf-8 -*-
"""
@author: Yi_Zhou
"""
import random

from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from testone.settings import *

def genrandom_str(randomlenght):
    str = ''
    chars = 'QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm0123456789.'
    lenght = [i for i in range(len(chars)-1)]
    for i in range(randomlenght):
        j = random.choice(lenght)
        str += chars[j:j+1]
    return str

def send_register_email(email, send_type):
    email_record = EmailVerifyRecord()
    random_str = genrandom_str(16)
    email_record.code = random_str
    email_record.email = email
    email_record.send_type = send_type
    # email_record.save()

    if send_type == "register":
        email_title = "注册链接！"
        email_body = "激活链接：http://127.0.0.1:8000/active/{0}".format(random_str)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            print("激活成功！")


