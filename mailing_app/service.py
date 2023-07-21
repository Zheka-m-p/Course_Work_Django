from mailing_app.models import Settings, AttemptMailing
import datetime
from mailing_app.sup_service import test_send_mail


def auto_mailing():
    '''Эта функция должна потом автоматически заполнять посленюю таблицу про попытку рассылки'''
    print('Проверка связи\n')
    distribution_list = Settings.objects.all().filter(
        status=Settings.STATUS_LAUNCHED)  # список всех рассылок, которые запущены!

    for one_spam_settings in distribution_list:  # Выбираем каждую рассылку отдельно и работает с ней, пытаемся отправить письма

        obj = AttemptMailing.objects.filter(settings_pk=one_spam_settings.id).last() # объект последнего заполнения БД-попыток
        if obj is None:
            time_now = datetime.datetime.now().time().replace(second=0, microsecond=0)  # текущее время
            last_attempt_date_time = one_spam_settings.time.replace(second=0, microsecond=0)  # время последней рассылки

            if last_attempt_date_time == time_now:  # можно убрать "иф" для проверки вообще работы по команде
                test_send_mail(one_spam_settings)  # работает(заполняет) при ручном запуске скрипта

        else:
            period = one_spam_settings.period
            last_attempt_date_time = obj.last_attempt_date_time
            print(last_attempt_date_time)

            if period == Settings.PERIOD_DAY:
                last_attempt_date_time += datetime.timedelta(days=1)
            elif period == Settings.PERIOD_WEEK:
                last_attempt_date_time += datetime.timedelta(days=7)
            elif period == Settings.PERIOD_MONTH:
                last_attempt_date_time += datetime.timedelta(days=30)

            last_attempt_date_time = last_attempt_date_time.replace(second=0, microsecond=0)
            time_now = datetime.datetime.now().replace(second=0, microsecond=0)

            if last_attempt_date_time == time_now:  # можно убрать "иф" для проверки вообще работы по команде
                test_send_mail(one_spam_settings)  # работает(заполняет) при ручном запуске скрипта
