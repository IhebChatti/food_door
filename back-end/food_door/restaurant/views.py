from restaurant.models import Restaurant, RestaurantImage
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from restaurant.serializers import RestaurantSerializer, ImageSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView
import json


######################### LIST RESTAURANTS #####################################

@api_view(['GET'])
@permission_classes([permissions.AllowAny, ])
def list_restaurants(request):
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

######################### LIST RESTAURANTS #####################################

@api_view(['GET'])
@permission_classes([permissions.AllowAny, ])
def get_restaurant_by_id(request):
    try:
        restaurant_id = request.GET.get('restaurant_id')
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
        except:
            return Response({'Error', 'No restaurant found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = RestaurantSerializer(restaurant)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'Internal server error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


######################### CREATE RESTAURANT #####################################


@api_view(['POST'])
@permission_classes([permissions.AllowAny, ])
def create_restaurant(request):
    try:
        restaurant_data = request.data
        serialized = RestaurantSerializer(data=restaurant_data)
        if serialized.is_valid():
            restaurant = Restaurant.objects.create(
                name=serialized.data['name'],
                description=serialized.data['description'],
                phone=serialized.data['phone'],
                address=serialized.data['address'],
            )
            restaurant.save()
            return Response({'message': 'created'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


######################### UPLOAD IMAGE #####################################

class ImageViewSet(ListAPIView):
    queryset = RestaurantImage.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        restaurant_id = request.data['restaurant_id']
        restaurant = Restaurant.objects.get(id=int(restaurant_id))
        file = request.data['file']
        name = restaurant.name
        image_instance = RestaurantImage.objects.create(name=name, image=file, restaurant=restaurant)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

    def get(self, request):
        try:
            restaurant_id = request.GET.get('restaurant_id')
            try:
                restaurant = Restaurant.objects.get(id=restaurant_id)
            except:
                return Response({'Error': 'No restaurant found by this id'})
            try:
                image = RestaurantImage.objects.get(restaurant=restaurant)
            except:
                return Response({'Error': 'No image found'})
            serializer = ImageSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {'error': 'Something went wrong deleting restaurant'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


######################### DELETE BY ID #####################################

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny, ])
def delete_restaurant_by_id(request):
    try:
        restaurant_id = request.GET.get('restaurant_id')
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
        except Exception:
            return Response({'Fail': "Restaurant by this id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        restaurant.delete()
        restaurant.save()

        return Response(
            {'Success': 'Restaurant deleted'},
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'Something went wrong deleting restaurant'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
