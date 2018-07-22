from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from workout.models import WorkoutPackage
from workout.serializers.workout_serializer import WorkoutPackageSerializer


class WorkoutPackageListView(APIView):
    permission_classes = permissions.AllowAny

    def get(self, request, *args, **kwargs):
        type = request.data["type"]
        packages = WorkoutPackage.objects.filter(type=type)
        serializer = WorkoutPackageSerializer(packages, many=True)
        result = serializer.data
        return Response(result, status=status.HTTP_200_OK)