from django.core.management import BaseCommand
from mailing_app.service import auto_mailing

class Command(BaseCommand):

    def handle(self, *args, **options):
        auto_mailing()