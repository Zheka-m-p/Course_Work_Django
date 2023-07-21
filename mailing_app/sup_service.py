from django.core.mail import send_mail
from django.conf import settings

from mailing_app.models import *

import pytz
import datetime

# send_mail(
#     subject='Получена новая ачивка: читающий жук',
#     message=f'Поздравляем, ваша статья  {obj.title} набрала {x} просмотров',
#     from_email=settings.EMAIL_HOST_USER,
#     recipient_list=['Chernik.dota@mail.ru'],
# )

def test_send_mail(one_spam_settings):
    # one_spam_settings - это одна настройка для рассылки писем, в которую мы хотим запустить и разослать все письма
    '''Текущий вариант функции отправляет вручную все рассылки на все адреса из них при запуске скрипта
        для этого надо в параметр передать оду из "настройка рассылки" '''
    print('Я работаю через WSL\n')
    emails_obj = one_spam_settings.addresses_spam.all()  # Адреса и имена,  но в несовсем нужном формате
    emails = [i.email for i in emails_obj]

    dump_bd_AttemptMailing = []  # пустой список, чтобы потом его заполнить для таблицы "попытка рассылки"
    for mail in emails:

        try:
            # print(mail)
            send_mail(
                subject=one_spam_settings.message.title,
                message=one_spam_settings.message.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[mail],
                fail_silently=False,
            )
        except:
            print(f'{mail} - РАССЫЛКА НЕ УДАЛАСЬ')
            server_response = {
                # 'last_attempt_date_time': datetime.datetime.now(), # можно убрать. т.е. стоит автозаполнение в моделе
                'status': 'not_delivered',
                'server_response': mail,
                'settings_pk': Settings.objects.get(pk=one_spam_settings.id)
            }
            dump_bd_AttemptMailing.append(AttemptMailing(**server_response))

        else:
            print(f'{mail} - РАССЫЛКА УДАЛАСЬ')
            server_response = {
                # 'last_attempt_date_time': datetime.datetime.now(), # можно убрать. т.е. стоит автозаполнение в моделе
                'status': 'delivered',
                'server_response': mail,
                'settings_pk': Settings.objects.get(pk=one_spam_settings.id)

            }
            dump_bd_AttemptMailing.append(AttemptMailing(**server_response))

    AttemptMailing.objects.bulk_create(dump_bd_AttemptMailing)

    print('Окончание работы одной рассылки\n')
