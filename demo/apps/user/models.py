from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator


# Usuario
class User(AbstractUser):
    username = models.CharField("Nombre Usuario", unique=True, max_length=50, validators=[RegexValidator(r'^[a-zA-Z0-9]+$', 'Solo se permiten letras y dígitos en este campo.')])
    email = models.EmailField(unique=True, max_length=40, verbose_name='email address')
    iniciales = models.CharField("Iniciales del Usuario", unique=True, max_length=4, validators=[RegexValidator(r'^[a-zA-Z0-9]+$', 'Solo se permiten letras y dígitos en este campo.')])
    groups = models.ManyToManyField('auth.Group', related_name="group_user_set", blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='userSet', blank=True)
    objects = UserManager()

    def __str__(self):
        return self.username