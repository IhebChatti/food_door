from django.db import models
from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _


############### User model ##############
class User(models.Model):
    first_name      = models.CharField(max_length=254, null=False)
    last_name       = models.CharField(max_length=254, null=False)
    email           = models.EmailField(_('email address'), max_length=254, unique=True, validators=[EmailValidator])
    password        = models.CharField(max_length=254, null=False)
    address         = models.CharField(max_length=254, null=False)
    phone           = models.CharField(max_length=100, null=True)
    is_verified     = models.BooleanField(default=False, null=True)

    EMAIL_FIELD     = 'email'
    REQUIRED_FIELDS = []

    @property
    def full_name(self): return str(self.first_name) + " " + str(self.last_name)

    def verify_email(self):
        self.is_verified = True
        self.save()

    class Meta(object):
        db_table            = 'user'
        verbose_name        = 'User'
        verbose_name_plural = 'Users'

