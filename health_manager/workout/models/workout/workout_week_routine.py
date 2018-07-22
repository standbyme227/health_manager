from django.db import models

from workout.models import WorkoutType, WorkoutPackage

WEEKDAY_CHOICES = (
    (0, '월요일'),
    (1, '화요일'),
    (2, '수요일'),
    (3, '목요일'),
    (4, '금요일'),
    (5, '토요일'),
    (6, '일요일'),
)



class WeekRoutine(WorkoutType):
    '''
    한 주에 어떤 루틴을 할것인지를 모아둔 모델
    '''
    week_day = models.SmallIntegerField('요일을 정한다.', choices=WEEKDAY_CHOICES)
    workout_package = models.ManyToManyField(WorkoutPackage, related_name='week_routines',)
