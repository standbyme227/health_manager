from .workout_type import *
from .workout_detail import *
from .workout_set import *
from .workout_routine import *
from .workout_routine_to_workout_set import *
from .workout_week_routine import *
from .workout_package import *
from .workout_package_to_week_routine import *









# from django.db import models
#
# # Create your models here.
#
# # class  TypeOfWorkout(models.Model):
# #     '''
# #        할 운동의 타입... 전신, 하체, 상체
# #     '''
# #     name = models.CharField('운동종류 이름', max_length=30)
# #     description = models.CharField('운동종류 설명', max_length=200)
#
#
# WORKOUT_TYPE_CHOICES = (
#     ('full', '전신 운동'),
#     ('upper', '상체 운동'),
#     ('lower', '하체 운동'),
# )
#
# WEEKDAY_CHOICES = (
#     (0, '월요일'),
#     (1, '화요일'),
#     (2, '수요일'),
#     (3, '목요일'),
#     (4, '금요일'),
#     (5, '토요일'),
#     (6, '일요일'),
# )
#
#
# class WorkoutType(models.Model):
#     workout_type = models.CharField('운동의 타입', choices=WORKOUT_TYPE_CHOICES)
#
#
# class WorkoutPackage(WorkoutType):
#     '''
#     루틴을 모아서 하나의 Package로 만든 모델
#     초급 턱걸이, 중급 턱걸이, 초급 푸쉬업 등등.
#     '''
#     name = models.CharField('운동세트 이름', max_length=40)
#     description = models.CharField('운동세트 설명', max_length=200)
#     weeks = models.SmallIntegerField('총 주차', max_length=10)
#
#
# class WeekRoutine(WorkoutType):
#     '''
#     한 주에 어떤 루틴을 할것인지를 모아둔 모델
#     '''
#     week_day = models.SmallIntegerField('요일을 정한다.', choices=WEEKDAY_CHOICES)
#     workout_package = models.ManyToManyField(WorkoutPackage, related_name='week_routines',)
#
# class Routine(WorkoutType):
#     '''
#     세트들을 모아서 루틴을 생성하기 위한 모델
#     '''
#
#     name = models.CharField('루틴 이름', max_length=40)
#     week_routine = models.ForeignKey(WeekRoutine, related_name='routines')
#
#
# class WorkoutPackageToWeekRoutine(models.Model):
#     '''
#         Package와 Routine을 이어주는 model
#         몇주차의 운동인지
#     '''
#
#     workout_package = models.ForeignKey(WorkoutPackage, related_name='routines', on_delete=models.CASCADE)
#     week_routine = models.ForeignKey(WeekRoutine, related_name='packages', on_delete=models.CASCADE)
#     week = models.SmallIntegerField('각 주차', max_length=10)
#
#
# class WorkoutSet(models.Model):
#     '''
#     각 세트에 맞는 횟수를 지정하기 위한 모델
#     '''
#     count = models.SmallIntegerField('한 번 할때의 운동 횟수', max_length=10, )
#     time = models.SmallIntegerField('한 번 할때의 운동 제한 시간', max_length=10)
#     # grade = models.SmallIntegerField('운동 등급', max_length=10)
#     # 운동 등급은 따로 빼서 모델링을 해야할거 같다.
#     routine = models.ManyToManyField(Routine, through='RoutineToWorkoutSet')
#
#
# class RoutineToWorkoutSet(models.Model):
#     routine = models.ForeignKey(Routine, related_name='workout_sets', on_delete=models.CASCADE)
#     workout_set = models.ForeignKey(WorkoutSet, related_name='routines', on_delete=models.CASCADE)
#     order = models.SmallIntegerField('운동 순서', max_length=10)
#
#
# class WorkoutDetail(WorkoutType):
#     '''
#     세세한 운동들 풀업, 친업, 내로우풀업, 와이드 풀업, 베이직 푸쉬업, 와이드 푸쉬업 등등
#     '''
#     name = models.CharField('운동 이름', max_length=20)
#     description = models.CharField('운동 설명', max_length=200)
#     workout_set = models.ForeignKey(WorkoutSet)
