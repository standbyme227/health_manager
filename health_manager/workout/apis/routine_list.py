from django.utils.timezone import localtime, now
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView




class RoutineListView(APIView):
    permission_classes = permissions.AllowAny

    def get(self, request, *args, **kwargs):
        package_id = request.data["package"]
        if package_id is None:
            data = "잘못된 package 넘버 입니다."
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

        from workout.models import WorkoutPackageToWeekRoutine
        try:
            week_routine = WorkoutPackageToWeekRoutine.objects.filter(week=None).get(package_id=package_id).week_routine
        except WorkoutPackageToWeekRoutine.DoesNotExist:
            data = 'package가 비어있습니다.'
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)




        # weekday = localtime(now()).weekday()



        # if weekday != 0:
