from rest_framework.permissions import BasePermission


class KakaoUserPermissions(BasePermission):
    def has_permission(self, request, view):
        return True