from rest_framework import serializers
from .models import Event as EventModel

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = "__all__"

    def update(self, instance, validated_data):
        for key, value in validated_data.items(): #요청이 Key:value 딕셔너리로 오므로 분리
            setattr(instance, key, value) #이 함수는 instance.key = value로 인식하게 바꿔줌. event.title = '바꾼제목'
                                         # 업데이트를 하려면 유저에게 받아온 해당정보들을 key : value에 맞게 수정해야지
        instance.save()
        return instance