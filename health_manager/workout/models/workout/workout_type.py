from django.db import models


WORKOUT_TYPE_CHOICES = (
    ('full', '전신 운동'),
    ('upper', '상체 운동'),
    ('lower', '하체 운동'),
)

class WorkoutType(models.Model):
    workout_type = models.CharField('운동의 타입', choices=WORKOUT_TYPE_CHOICES)



