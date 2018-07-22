from django.db import models



class WorkoutPackageToWeekRoutine(models.Model):
    '''
        Package와 Routine을 이어주는 model
        몇주차의 운동인지
    '''

    workout_package = models.ForeignKey(WorkoutPackage, related_name='routines', on_delete=models.CASCADE)
    week_routine = models.ForeignKey(WeekRoutine, related_name='packages', on_delete=models.CASCADE)
    week = models.SmallIntegerField('각 주차', max_length=10)

