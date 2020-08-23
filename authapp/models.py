from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', verbose_name='аватар', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='возраст')
    email = models.CharField(verbose_name='e-mail', max_length=100)

    GENDER_CHOICES = [
        (True, 'male'),
        (False, 'female')
    ]
    gender = models.BooleanField(verbose_name='пол', choices=GENDER_CHOICES, default=True)

    RUSSIA = 'Ru'
    UKRAINE = 'Ukr'
    CHINA = 'Ch'
    COUNTRY_CHOICES = [
        (RUSSIA, 'Russia'),
        (UKRAINE, 'Ukraine'),
        (CHINA, 'China'),
    ]
    country = models.CharField(verbose_name='страна', max_length=100, choices=COUNTRY_CHOICES, blank=True)