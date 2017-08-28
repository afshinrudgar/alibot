import random

from django.utils import timezone

from alibot.bot.models import CodeStore


class VerificationError(Exception):
    pass


class AuthService(object):

    @staticmethod
    def create_code(guardian):
        code = random.randint(1000, 9999)
        obj = CodeStore.objects.update_or_create(
            guardian=guardian,
            defaults={'code': code, 'last_update': timezone.now()}
        )
        return obj.code

    @staticmethod
    def verify(guardian, code):
        if guardian.code_store.code == code:
            guardian.code_store.verified = True
            guardian.code_store.save()
        else:
            raise VerificationError
