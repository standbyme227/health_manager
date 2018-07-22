from rest_framework import serializers

from members.models import User


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = '__all__'
