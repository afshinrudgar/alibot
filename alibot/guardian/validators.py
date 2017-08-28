import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


@deconstructible
class PhoneNumberValidator(object):
    """
    Validator to check is a phone number is valid
    """

    message = _('Ensure that phone number is valid.')
    code = 'phone number'
    patterns = [
        r'^(?:(\+98|00980|0098|980|98)|0)(\d{4,11})$',
    ]

    def __init__(self, message=None):
        self.message = message or self.message
        self.checkers = [re.compile(p) for p in self.patterns]

    def __call__(self, value):
        if value is not None:
            value = re.sub(r'(\-|\(|\)|\s|\.\d+)', '', value)
            for checker in self.checkers:
                if checker.match(value):
                    return
        raise ValidationError(self.message, code=self.code, params={'patterns': self.patterns})


@deconstructible
class MobileNumberValidator(PhoneNumberValidator):
    """
    Validator to check if a mobile number is valid
    """

    message = _('Ensure that mobile number is valid.')
    code = 'mobile number'
    # range of mobile numbers are : [901-939|990]
    patterns = [r'^(0|0{0,2}98|\+98){0,1}(9([1-3]\d|0[1-9]|90)\d{7})$']


