from django.contrib.auth.models import UserManager
from django.db import models
from django.core.validators import EmailValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser

############### User model ##############
class User(AbstractBaseUser):
    first_name      = models.CharField(max_length=254, null=False)
    last_name       = models.CharField(max_length=254, null=False)
    email           = models.EmailField(_('email address'), max_length=254, unique=True, validators=[EmailValidator])
    password        = models.CharField(max_length=254, null=False)
    address         = models.CharField(max_length=254, null=False)
    phone           = models.CharField(max_length=100, null=True)
    is_verified     = models.BooleanField(default=False, null=True)
    last_login      = models.DateTimeField(null=True)

    USERNAME_FIELD  = 'email'
    EMAIL_FIELD     = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def full_name(self): return str(self.first_name) + " " + str(self.last_name)

    def verify_email(self):
        self.is_verified = True
        self.save()

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return False


    class Meta(object):
        db_table            = 'user'
        verbose_name        = 'User'
        verbose_name_plural = 'Users'

class UserLoginActivity(models.Model):
    login_IP        = models.GenericIPAddressField(null=True)
    login_datetime  = models.DateTimeField(auto_now=True)
    login_username  = models.CharField(max_length=40, null=True)
    status          = models.CharField(max_length=40, default='success', null=True)
    user_agent_info = models.CharField(max_length=255)
    class Meta:
        db_table            = 'user_login_activity'
        verbose_name        = 'Login Activity'
        verbose_name_plural = 'Login Activities'

