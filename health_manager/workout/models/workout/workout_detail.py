from django.db import models

from workout.models import WorkoutType, WorkoutSet


class WorkoutDetail(WorkoutType):
    '''
    세세한 운동들 풀업, 친업, 내로우풀업, 와이드 풀업, 베이직 푸쉬업, 와이드 푸쉬업 등등
    '''
    name = models.CharField('운동 이름', max_length=20)
    description = models.CharField('운동 설명', max_length=200)
    workout_set = models.ForeignKey(WorkoutSet)
