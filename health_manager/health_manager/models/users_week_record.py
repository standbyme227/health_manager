from django.conf import settings
from django.db import models

# Create your models here.
from workout.models import WeekRoutine



class UsersWeekRecord(models.Model):
    '''
        오늘 할 루틴을 1주일치 모은 1주일 기록
    '''
    user = models.ForeignKey('일주일을 기록할 유저', settings.AUTH_MODEL_USER, related_name='week_records')
    week_routine = models.ForeignKey('이번주 루틴', WeekRoutine)
    week = models.SmallIntegerField('몇 주차인지', max_length=10, default=0)
    done = models.BooleanField('한 주 루틴 완료여부')

