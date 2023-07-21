from django.core.management import BaseCommand
from mailing_app.service import auto_mailing
from mailing_app.sup_service import test_send_mail

class Command(BaseCommand):

    def handle(self, *args, **options):
        auto_mailing()
        # test_send_mail() # старая версия, но пришлось переделать, чтобы не дублировать код