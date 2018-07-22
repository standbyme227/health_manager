from rest_framework.views import APIView
from health_manager.models import UsersHealthCoach
from members import permissions


class HealthCoachCreateView(APIView):
    permission_classes = permissions.KakaoUserPermissions

    def post(self, request, *args, **kwargs):
        user = request.user
        package = request.data["package"]
        health_coach = UsersHealthCoach.objects.create(
            client=user.id,
            package = package
        )
