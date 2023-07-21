from mailing_app.models import Client
from random import randint

def add_rand_client():
    '''Должна функия добавлять клиента с рандомными данными, но не работает....'''
    print('Долбанный кронжоп!!!')
    a, b, c =  [randint(0, 100) for _ in range(3)]
    Client.objects.create(email=a, fio=b, comment=c)
