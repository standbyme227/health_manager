from django.conf import settings
from django.db import models

# Create your models here.
from workout.models import WorkoutPackage, WorkoutDetail, Routine



class TodayWorkout(models.Model):
    '''
        최소단위 오늘할 운동의 가장 작은 단위
    '''
    workout = models.ForeignKey('오늘 할 운동', WorkoutDetail)
    count = models.SmallIntegerField(max_length=10)
    done = models.BooleanField('하루 운동 완료 여부', default=False)

class TodayRoutine(models.Model):
    '''
        오늘 할 운동들이 모인 루틴
    '''
    routine =  models.ForeignKey('오늘 할 루틴', Routine)
    achievement_rate = models.DecimalField('달성률', )
    done = models.BooleanField('하루 루틴 완료 여부', default=False)
    today_workouts = models.ForeignKey('오늘의 루틴', TodayWorkout)
    order = models.SmallIntegerField('패키지 안에서의 루틴 순서', max_length=10)

class WeekRecord(models.Model):
    '''
        오늘 할 루틴을 1주일치 모은 1주일 기록
    '''
    week = models.SmallIntegerField('몇 주차인지', max_length=10)
    week_routine = models.ForeignKey('오늘한 루틴', )
    done = models.BooleanField('한 주 루틴 완료여부')

class CheckClientForWorkout(models.Model):
    '''
        1주일치 기록들을 모아서 패키지의 완성을 체크하는 곳
    '''

    client = models.ForeignKey('운동을 시작한 User', settings.AUTH_MODEL_USER, related_name='client_health_manager')
    workout_package = models.ForeignKey('선택한 Package', WorkoutPackage, related_name='started_health_manager')
    name = models.CharField('운동 계획 이름',max_length=100)
    done = models.BooleanField('패키지 완료여부', default=False)
    week_record = models.ForeignKey('Package 기록', WeekRecord)