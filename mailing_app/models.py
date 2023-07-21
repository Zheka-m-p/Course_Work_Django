from django.db import models


class Client(models.Model):
    email = models.EmailField(verbose_name='email')
    fio = models.CharField(verbose_name='ФИО', max_length=150)
    comment = models.TextField(verbose_name='комментарий')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return f'{self.fio}, {self.email}'


# class SettingMailing()
class Settings(models.Model):
    PERIOD_DAY = 'day'
    PERIOD_WEEK = 'week'
    PERIOD_MONTH = 'month'

    PERIODS = (
        (PERIOD_DAY, 'день'),
        (PERIOD_WEEK, 'неделя'),
        (PERIOD_MONTH, 'месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_LAUNCHED = 'launched'
    STATUS_COMPLETED = 'completed'

    STATUSES = (
        ('created', 'создана'),
        ('launched', 'запущена'),
        ('completed', 'завершена'),  # можно завершить, но только вручную. т.к. рассылка периодическая
    )

    time = models.TimeField(verbose_name='время рассылки')
    period = models.CharField(max_length=15, choices=PERIODS, default=PERIOD_DAY,
                              verbose_name='периодичность расссылки')
    status = models.CharField(max_length=15, choices=STATUSES, default=STATUS_CREATED, verbose_name='статус рассылки')

    message = models.ForeignKey('mailing_app.Message', on_delete=models.CASCADE, verbose_name='сообщение')
    addresses_spam = models.ManyToManyField('mailing_app.Client', verbose_name='адреса для рассылок')

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройка рассылок'

    def __str__(self):
        return f'{self.time}, {self.period}, {self.status}, {self.message}'


class Message(models.Model):
    title = models.CharField(max_length=80, verbose_name='тема сообщения')
    body = models.TextField(verbose_name='тело сообщения')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return f'{self.title}'


# class ClientAddress(models.Model):
#     '''Такой тоже есть вариант(расшивка), если сделать доп модель, в которой будут все адреса для конкретной рассылки'''
#     client = models.ForeignKey('mailing_app.Client', on_delete=models.CASCADE, verbose_name='адрес клиента для рассылки')
#     settings = models.ForeignKey('mailing_app.Settings', on_delete=models.CASCADE, verbose_name='найстрока-ключ')
class AttemptMailing(models.Model):
    STATUS_DELIVERED = 'delivered'
    STATUS_NOT_DELIVERED = 'not_delivered'

    STATUSES = (
        ('delivered', 'доставлено'),
        ('not_delivered', 'не доставлено'),
    )

    last_attempt_date_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки рассылки')
    status = models.CharField(max_length=15, choices=STATUSES, default=STATUS_DELIVERED, verbose_name='статус')
    server_response = models.CharField(blank=True, max_length=100, verbose_name='ответ сервера, если он был')

    settings_pk = models.ForeignKey(Settings, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылок'

    def __str__(self):
        return f'{self.last_attempt_date_time} {self.status} {self.server_response} '
