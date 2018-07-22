from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from workout.models import WorkoutPackage
from workout.serializers.workout_serializer import WorkoutPackageSerializer


class WorkoutPackageDetailView(APIView):
    permission_classes = permissions.AllowAny

    def get(self, request, *args, **kwargs):
        package_id = request.data['package']
        try:
            package = WorkoutPackage.objects.get(id=package_id)
        except WorkoutPackage.DoesNotExist:
            data = 'WorkoutPackage matching query does not exist'
            return Response(data=data, status=status.HTTP_403_FORBIDDEN)
        serializer = WorkoutPackageSerializer(package)
        result = serializer.data
        return Response(result, status=status.HTTP_200_OK)


