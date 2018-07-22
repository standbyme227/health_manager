from django.conf import settings
from django.db import models

# Create your models here.
# from health_manager.models import UsersWeekRecord
from workout.models import WorkoutPackage

class UsersHealthCoach(models.Model):
    '''
        1주일치 기록들을 모아서 패키지의 완성을 체크하는 곳
    '''

    user = models.ForeignKey('운동을 시작한 User', settings.AUTH_MODEL_USER, related_name='health_coaches')
    workout_package = models.ForeignKey('선택한 Package', WorkoutPackage, related_name='health_coaches')
    name = models.CharField('운동 계획 이름',max_length=100, blank=True, null=True)
    done = models.BooleanField('패키지 완료여부', default=False)
    # week_record = models.ForeignKey('Package 기록', UsersWeekRecord, blank=True, null=True)