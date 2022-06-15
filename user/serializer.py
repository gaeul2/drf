from rest_framework import serializers
from .models import User as UserModel
from .models import UserProfile as UserProfileModel
from .models import Hobby as HobbyModel


class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()

    def get_same_hobby_users(self, obj):
        user_list = []
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.fullname)

        return user_list

    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]


class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "hobby"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = UserModel
        fields = ["username", "fullname", "password", "email", "join_date", "userprofile"]
        extra_kwargs = {
            'password': {'write_only': True},
        }


