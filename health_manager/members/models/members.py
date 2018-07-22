from django.core.validators import MaxValueValidator
from django.db import models
from members.models import User


class Member(models.Models):
    user = models.OneToOneField(User)

    user_num = models.CharField('회원등록번호', max_length=20)
    name = models.CharField('이름', max_length=10, blank=True)
    height = models.SmallIntegerField('키', max_length=10, blank=True)
    weight = models.DecimalField('몸무게', max_digits=5, decimal_places=2,
                                 validators=[MaxValueValidator(999), ], blank=True)

    # grade = models.SmallIntegerField('등급', max_length=10)
