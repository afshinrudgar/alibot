from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        from alibot.bot import updater
        updater.start_polling()
        self.stdout.write(self.style.SUCCESS('Bot started'))
        updater.idle()
