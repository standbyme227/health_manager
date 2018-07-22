from django.db import models
from members.models import User


class Member(models.Models):
    user = models.OneToOneField(User)

    user_num = models.SmallIntegerField('회원번호', max_length=10)

    name = models.CharField('이름', max_length=10)
    height = models.SmallIntegerField('키', max_length=10)
    weight = models.DecimalField('몸무게', )

    # grade = models.SmallIntegerField('등급', max_length=10)