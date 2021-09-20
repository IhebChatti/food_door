from restaurant.models import FoodItem, Restaurant, RestaurantImage, FoodImage
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from restaurant.serializers import FoodSerializer, ImageSerializer, FoodImageSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView
import json


######################### LIST RESTAURANTS #####################################

@api_view(['GET'])
@permission_classes([permissions.AllowAny, ])
def list_food(request):
    try:
        _food = FoodItem.objects.all()
        serializer = FoodSerializer(_food, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'no food'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

######################### LIST RESTAURANTS #####################################

@api_view(['GET'])
@permission_classes([permissions.AllowAny, ])
def get_food_by_id(request):
    try:
        food_id = request.GET.get('food_id')
        try:
            food = FoodItem.objects.get(id=food_id)
        except:
            return Response({'Error', 'No food found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = FoodSerializer(food)

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
def create_food(request):
    try:
        food_data = request.data
        serialized = FoodSerializer(data=food_data)
        if serialized.is_valid():
            food = FoodItem.objects.create(
                name=serialized.data['name'],
                description=serialized.data['description'],
                price=serialized.data['price'],
            )
            food.save()
            return Response(str('message: created'), status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


######################### DELETE BY ID #####################################

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny, ])
def delete_food_by_id(request):
    try:
        food_id = request.GET.get('food_id')
        try:
            food = FoodItem.objects.get(id=food_id)
        except Exception:
            return Response({'Fail': "food by this id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        food.delete()

        return Response(
            {'Success': 'food deleted'},
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'Something went wrong deleting food'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


######################### UPLOAD IMAGE #####################################

class ImageViewSetFood(ListAPIView):
    queryset = FoodImage.objects.all()
    serializer_class_image = FoodImageSerializer

    def post(self, request, *args, **kwargs):
        food_id = request.data['food_id']
        food = FoodItem.objects.get(id=int(food_id))
        file = request.data['file']
        name = food.name
        image_instance = FoodImage.objects.create(name=name, image=file, food=food)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

    def get(self, request):
        try:
            food_id = request.GET.get('food_id')
            try:
                food = FoodItem.objects.get(id=food_id)
            except:
                return Response({'Error': 'No food found by this id'})
            try:
                image = FoodImage.objects.get(food=food)
            except:
                return Response({'Error': 'No image found'})
            serializer = FoodImageSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {'error': 'Something went wrong on food image'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
