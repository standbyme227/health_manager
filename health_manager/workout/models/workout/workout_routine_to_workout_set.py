from django.db import models

from workout.models import Routine, WorkoutSet


class RoutineToWorkoutSet(models.Model):
    routine = models.ForeignKey(Routine, related_name='workout_sets', on_delete=models.CASCADE)
    workout_set = models.ForeignKey(WorkoutSet, related_name='routines', on_delete=models.CASCADE)
    order = models.SmallIntegerField('운동 순서', max_length=10)

