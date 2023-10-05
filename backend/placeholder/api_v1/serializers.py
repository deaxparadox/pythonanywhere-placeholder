from rest_framework import serializers

from ..models import UserInfo

class UserInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"


# class UserInfoSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     user = serializers.CharField()
#     email = serializers.EmailField()
#     address = serializers.CharField()
