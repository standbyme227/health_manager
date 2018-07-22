from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from members import permissions
from members.models import User
from members.models.members import Member
from members.serializers import UserSerializer


class UserCreateAPIView(APIView):
    permission_classes = permissions.KakaoUserPermissions

    def post(self, request, *args, **kwargs):

        data = request.data
        try:
            username = data["username"]
            if username is None:
                data = {"username": ["username을 입력해주세요."]}
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

            password = data["password"]
            if password is None:
                data = {"password": ["password를 입력해주세요."]}
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

            if len(User.objects.filter(username=username)) > 0:
                data = {"username": ["이미 사용중인 username 입니다."]}
                return Response(data=data, status=status.HTTP_409_CONFLICT)

            name = data["name"]
            if len(list(name)) > 10:
                data = {"name": ["이름이 너무 깁니다."]}
                return Response(data=data, status=status.HTTP_403_FORBIDDEN)

            height = data["height"]
            if height is None:
                height = ''

            if len(list(str(height))) > 3:
                data = {"height": ["키는 정수값으로 1~999 사이입니다."]}
                return Response(data=data, status=status.HTTP_403_FORBIDDEN)

            weight = data["weight"]
            if weight is None:
                weight = ''

            if len(list(str(weight))) > 7:
                data = {"weight": ["몸무게는 소수값으로 0.00~999.00사이입니다."]}
                return Response(data=data, status=status.HTTP_403_FORBIDDEN)

            user = User.objects.get_or_create(
                username = username,
                password = password
            )
            user_pk_list = list(str(user.pk))
            if len(user_pk_list) < 10:
                zero = '0'
                blank_count = 10 - len(user_pk_list)
                user_pk_list.insert(0, zero*blank_count)

            user_num = name + '-'+''.join(user_pk_list)

            member = Member.objects.get_or_create(
                user=user,
                user_num=user_num,
                name=name,
                height=height,
                weight=weight,
            )

            serializer = UserSerializer(user)
            result = serializer.data
        except Exception as ex:
            return Response('회원가입에 실패했습니다.', status=status.HTTP_400_BAD_REQUEST)





