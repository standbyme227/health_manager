from rest_framework.permissions import BasePermission

from members.models import User


class KakaoUserPermissions(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.filter(id=request.user.id)
        if len(user) > 0:
            return True
        return False

