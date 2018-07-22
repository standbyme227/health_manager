from rest_framework.views import APIView
from health_manager.models import HealthCoach
from members import permissions


class HealthCoachCreateView(APIView):
    permission_classes = permissions.KakaoUserPermissions

    def post(self, request, *args, **kwargs):
        user = request.user
        package = request.data["package"]
        health_coach = HealthCoach.objects.create(
            client=user.id,
            package = package
        )
