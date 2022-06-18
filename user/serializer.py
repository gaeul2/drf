from rest_framework import serializers
from .models import User as UserModel
from .models import UserProfile as UserProfileModel
from .models import Hobby as HobbyModel
from blog.models import Article as ArticleModel


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
    hobby = HobbySerializer(many=True, required=False)
    get_hobbys = serializers.ListField(required=False)
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "gender", "hobby", "get_hobbys"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = UserModel
        fields = ["username", "fullname", "password", "email", "join_date", "userprofile"]
        extra_kwargs = {
            'password': {'write_only': True},
            'email' : {
                #validator에서 해당필드 필요여부 판단
                'required' : True, #default : True
                #에러메세지를 자유롭게 설정가능.
                'error_messages':{
                    # 값이 입력되지 않았을때 보여지는 메세지
                    'required' : '이메일을 입력해주세요.',
                    # 값의 형태가 맞지 않을때 보여지는 메시지
                    'invalid' : '알맞은 형식의 이메일을 입력해 주세요.',
                    }
                }
            }

    def validate(self, data):
        # custom validation pattern
        # 데이터에서 userprofile이라는 키값을 가져오고, 그안에서 age를 가져옴
        #                                 없으면 {},         없으면 0
        if data.get("userprofile", {}).get("age", 0) < 12: #연령제한 걸어줌
            # validation에 통과하지 못할 경우 ValidationError class 호출
            raise serializers.ValidationError(
                # custom validation error message
                # detail로 내가 어떤 에러메세지 보낼지 설정해준것
                detail={"error": "12세 이상만 가입할 수 있습니다."},
            )

        # validation에 문제가 없을 경우 data return
        return data

    def create(self, validated_data):
        # object를 생성할때 다른 데이터가 입력되는 것을 방지하기 위해 미리 pop 해준다.
        user_profile = validated_data.pop('userprofile')
        get_hobbys = user_profile.pop("get_hobbys", [])

        # User object 생성
        user = UserModel(**validated_data)
        user.save()

        # UserProfile object 생성
        user_profile = UserProfileModel.objects.create(user=user, **user_profile)

        # hobby 등록
        user_profile.hobby.add(*get_hobbys)
        user_profile.save()

        return user


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ["title", "category", "content"]


class LoginUserSerializer(serializers.ModelSerializer):
    #ForeignKey인 Article를 불러오려하니 에러발생.
    # Article모델에서 related_name지정해주고, 시리얼라이저의 StringRelatedField로 바꾸니
    # 사용자가 작성한 게시글 정보 불러오기 성공. 위에 작성한 ArticleSerializer는 사용하지 못했지만..ㅠㅠ
    article = serializers.StringRelatedField(many=True)

    class Meta:
        model = UserModel
        fields = ["username", "fullname", "password", "email", "join_date", "article"]
        extra_kwargs = {
            'password': {'write_only': True},
        }

