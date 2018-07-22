from django.db import models

from workout.models import Routine


class WorkoutSet(models.Model):
    '''
    각 세트에 맞는 횟수를 지정하기 위한 모델
    '''
    count = models.SmallIntegerField('한 번 할때의 운동 횟수', max_length=10, )
    time = models.SmallIntegerField('한 번 할때의 운동 제한 시간', max_length=10)
    # grade = models.SmallIntegerField('운동 등급', max_length=10)
    # 운동 등급은 따로 빼서 모델링을 해야할거 같다.
    routine = models.ManyToManyField(Routine, through='RoutineToWorkoutSet')

