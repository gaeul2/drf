from datetime import datetime
from rest_framework import status
from .models import Event as EventModel
from product.serializer import EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class EventView(APIView):
    def get(self, request):
        today = datetime.now().date() # now().today()는 초까지 다나옴
        products = EventModel.objects.filter(
            show_start_date__lte=today,
            show_stop_date__gte=today,
            is_active=True
        )
        return Response(EventSerializer(products, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        event_serializer = EventSerializer(data=request.data)

        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=status.HTTP_200_OK)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateEvent(APIView):
    def put(self,request,event_id):
        edit_event = EventModel.objects.get(id=event_id) #부분수정가능하도록 partial=True
        event_serializer = EventSerializer(edit_event, data=request.data, partial=True)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=status.HTTP_200_OK)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

