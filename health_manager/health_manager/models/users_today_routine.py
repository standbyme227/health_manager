from django.conf import settings
from django.db import models

# Create your models here.
# from health_manager.models import UsersTodayWorkout
from workout.models import Routine


class UsersTodayRoutine(models.Model):
    '''
        오늘 할 운동들이 모인 루틴
    '''
    user = models.ForeignKey('오늘의 루틴을 할 유저', settings.AUTH_MODEL_USER, related_name='today_routine')
    # today_workouts = models.ForeignKey('오늘의 운동', UsersTodayWorkout)
    routine =  models.ForeignKey('오늘 할 루틴', Routine)

    achievement_rate = models.DecimalField('달성률', )
    done = models.BooleanField('하루 루틴 완료 여부', default=False)
    order = models.SmallIntegerField('패키지 안에서의 루틴 순서', max_length=10)
