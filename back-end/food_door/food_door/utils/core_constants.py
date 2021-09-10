from django.db import models


class UserType(models.IntegerChoices):  # noqa: WPS431
    MASTER = 1, 'master'
    ADMIN = 2, 'admin'
    MANAGER = 3, 'manager'
    USER = 4, 'user'
    PARTNER = 5, 'partner',
