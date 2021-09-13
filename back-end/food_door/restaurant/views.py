from restaurant.models import Restaurant, RestaurantImage
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from restaurant.serializers import RestaurantSerializer, ImageSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView
import json

@api_view(['GET'])
@permission_classes([permissions.AllowAny, ])
def get_restaurants(request):
    try:
        _restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(_restaurants, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'no retaurants'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['POST'])
@permission_classes([permissions.AllowAny, ])
def create_restaurant(request):
    try:
        restaurant_data = request.data
        serialized = RestaurantSerializer(data=restaurant_data)
        breakpoint()
        if serialized.is_valid():
            restaurant = Restaurant.objects.create(
                name=serialized.data['name'],
                description=serialized.data['description'],
                phone=serialized.data['phone'],
                address=serialized.data['address'],
                image=serialized.data['image'],
            )
            restaurant.save()
            return Response({'message': 'created'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ImageViewSet(ListAPIView):
    queryset = RestaurantImage.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = RestaurantImage.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)