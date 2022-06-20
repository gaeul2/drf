from rest_framework import status

from product.serializer import EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class CreateEvent(APIView):
    def post(self, request):
        product_serializer = EventSerializer(data=request.data)

        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
