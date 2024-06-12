from rest_framework import serializers
from .models import UserData


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "name", "password"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model = UserData
        fields = ["username_or_email", "password"]
    username_or_email = serializers.CharField()
    password = serializers.CharField()