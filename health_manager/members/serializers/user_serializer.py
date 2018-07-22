from rest_framework import serializers

from members.models import User
from members.models.members import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    member = MemberSerializer()

    class Meta:
        model = User
        fields = ['__all__', 'member']

