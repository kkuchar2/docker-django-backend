from django.core.management import call_command
from django.core.management.commands.runserver import Command as RunServerCommand


class Command(RunServerCommand):

    def handle(self, *args, **kwargs):
        #call_command('test')
        super().handle(*args, **kwargs)
