from django.db import models

from workout.models import WorkoutType, WeekRoutine


class Routine(WorkoutType):
    '''
    세트들을 모아서 루틴을 생성하기 위한 모델
    '''

    name = models.CharField('루틴 이름', max_length=40)
    week_routine = models.ForeignKey(WeekRoutine, related_name='routines')
