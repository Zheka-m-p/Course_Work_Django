from django.test import TestCase

# Create your tests here.


# def test_send_mail():
#     '''Текущий вариант функции отправляет вручную все рассылки на все адреса из них при запуске скрипта'''
#     print('Я работаю через WSL\n')
#
#     distribution_list = Settings.objects.all().filter(status='launched')  # список всех рассылок, которые запущены!
#     for element in distribution_list:  # Выбираем каждую рассылку отдельно и работает с ней, пытаемся отправить письма
#         emails_obj = element.addresses_spam.all()  # Адреса и имена,  но в несовсем нужном формате
#         emails = [i.email for i in emails_obj]  # почты списком на которые надо разослать ( для КАЖДОЙ рассылки свои )
#
#         dump_bd_AttemptMailing = []  # пустой список, чтобы потом его заполнить для таблицы "попытка рассылки"
#         for mail in emails:
#
#             try:
#                 # print(mail)
#                 fsf
#                 send_mail(
#                     subject=element.message.title,
#                     message=element.message.body,
#                     from_email=settings.EMAIL_HOST_USER,
#                     recipient_list=[mail],
#                     fail_silently=False,
#                 )
#             except:
#                 print(f'{mail} - РАССЫЛКА НЕ УДАЛАСЬ')
#                 server_response = {
#                     # 'last_attempt_date_time': datetime.datetime.now(), # можно убрать. т.е. стоит автозаполнение в моделе
#                     'status': 'not_delivered',
#                     'server_response': mail,
#                     'settings_pk': Settings.objects.get(pk=element.id)
#                 }
#                 dump_bd_AttemptMailing.append(AttemptMailing(**server_response))
#
#             else:
#                 print(f'{mail} - РАССЫЛКА УДАЛАСЬ')
#                 server_response = {
#                     # 'last_attempt_date_time': datetime.datetime.now(), # можно убрать. т.е. стоит автозаполнение в моделе
#                     'status': 'delivered',
#                     'server_response': mail,
#                     'settings_pk': Settings.objects.get(pk=element.id)
#
#                 }
#                 dump_bd_AttemptMailing.append(AttemptMailing(**server_response))
#
#         AttemptMailing.objects.bulk_create(dump_bd_AttemptMailing)
#
#         print('Окончание работы одной рассылки\n')
#
#
# def auto_mailing():
#     '''Эта функция должна потом автоматически заполнять посленюю таблицу про попытку рассылки'''
#     # На текущий момент делает то же что и прошлая функция, осталось добавить работу с кронжопой
#     print('Проверка связи\n')
#     distribution_list = Settings.objects.all().filter(status='launched')  # список всех рассылок, которые запущены!
#
#     print(distribution_list, 'это дистрибутион лист')
#
#     for one_spam_settings in distribution_list:  # Выбираем каждую рассылку отдельно и работает с ней, пытаемся отправить письма
#
#         test_send_mail(one_spam_settings)