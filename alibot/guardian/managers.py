from django.contrib.auth.base_user import BaseUserManager


def normalize_mobile_number(num):
    num = num[4:] if num.startswith('0098') else num
    return num


class GuardianManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, mobile_number, password='unused-password', **extra_fields):
        """
        Creates and saves a User with the given mobile_number and password.
        """
        if not mobile_number:
            raise ValueError('The given mobile_number must be set')
        mobile_number = normalize_mobile_number(mobile_number)
        user = self.model(email=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile_number, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile_number, password, **extra_fields)

    def get_by_telegram_id(self, tid):
        return self.get(telegram_id=tid)

    def create_superuser(self, mobile_number, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(mobile_number, password, **extra_fields)
