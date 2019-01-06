from django.core.management.base import BaseCommand
from home.models import Member


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Done')