from rest_framework import serializers
from workout.models import WorkoutPackage


class WorkoutPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPackage
        fields = '__all__'


