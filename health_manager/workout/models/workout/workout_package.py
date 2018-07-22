from django.db import models

from workout.models import WorkoutType


class WorkoutPackage(WorkoutType):
    '''
    루틴을 모아서 하나의 Package로 만든 모델
    초급 턱걸이, 중급 턱걸이, 초급 푸쉬업 등등.
    '''
    name = models.CharField('운동세트 이름', max_length=40)
    description = models.CharField('운동세트 설명', max_length=200)
    weeks = models.SmallIntegerField('총 주차', max_length=10)
