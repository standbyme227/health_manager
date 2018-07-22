from django.db import models


# Create your models here.


class WorkoutPackage(models.Model):
    '''
    루틴을 모아서 하나의 Package로 만든 모델
    초급 턱걸이, 중급 턱걸이, 초급 푸쉬업 등등.
    '''
    name = models.CharField('운동세트 이름', max_length=40)
    description = models.CharField('운동 설명', max_length=200)
    weeks = models.SmallIntegerField('총 주차', max_length=10)


class Routine(models.Model):
    '''
    세트들을 모아서 루틴을 생성하기 위한 모델
    '''

    name = models.CharField('루틴 이름', max_length=40)
    workout_package = models.ManyToManyField(WorkoutPackage)


class WorkoutSet(models.Model):
    '''
    각 세트에 맞는 횟수를 지정하기 위한 모델
    '''
    count = models.SmallIntegerField('한 번 할때의 운동 횟수', max_length=10, )
    time = models.SmallIntegerField('한 번 할때의 운동 제한 시간', max_length=10)
    # grade = models.SmallIntegerField('운동 등급', max_length=10)
    # 운동 등급은 따로 빼서 모델링을 해야할거 같다.
    routine = models.ManyToManyField(Routine, through='RoutineToWorkoutSet')


class RoutineToWorkoutSet(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    workout_set = models.ForeignKey(WorkoutSet, on_delete=models.CASCADE)
    order = models.SmallIntegerField('운동 순서', max_length=10)


class WorkoutDetail(models.Model):
    '''
    세세한 운동들 풀업, 친업, 내로우풀업, 와이드 풀업, 베이직 푸쉬업, 와이드 푸쉬업 등등
    '''
    name = models.CharField('운동 이름', max_length=20)
    description = models.CharField('운동 설명', max_length=200)
    workout_set = models.ForeignKey(WorkoutSet)