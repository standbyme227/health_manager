from django.conf import settings
from django.db import models

# Create your models here.
from workout.models import WorkoutDetail


class UsersTodayWorkout(models.Model):
    '''
        최소단위 오늘할 운동의 가장 작은 단위
    '''
    user = models.ForeignKey('일주일을 기록할 유저', settings.AUTH_MODEL_USER, related_name='week_records')
    workout = models.ForeignKey('오늘 할 운동', WorkoutDetail)
    count = models.SmallIntegerField(max_length=10)
    done = models.BooleanField('하루 운동 완료 여부', default=False)