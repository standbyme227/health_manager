from rest_framework import generics

from members import permissions
from members.models import User
from members.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = permissions.KakaoUserPermissions
    serializer_class =  UserSerializer
    queryset = User.objects.all()