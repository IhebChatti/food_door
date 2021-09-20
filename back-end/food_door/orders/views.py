from restaurant.models import FoodItem, Restaurant, RestaurantImage, FoodImage
from orders.models import Order
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from orders.serializers import OrderSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView
import json


######################### LIST Orders #####################################

@api_view(['GET'])
@permission_classes([permissions.AllowAny, ])
def list_orders(request):
    try:
        _order = Order.objects.all()
        serializer = OrderSerializer(_order, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'no order'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

######################### GET Order #####################################

@api_view(['GET'])
@permission_classes([permissions.AllowAny, ])
def get_order_by_id(request):
    try:
        order_id = request.GET.get('order_id')
        try:
            order = Order.objects.get(id=order_id)
        except:
            return Response({'Error', 'No order found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'Internal server error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


######################### CREATE Order #####################################


@api_view(['POST'])
@permission_classes([permissions.AllowAny, ])
def create_order(request):
    try:
        order_data = request.data
        serialized = OrderSerializer(data=order_data)
        if serialized.is_valid():
            order = Order.objects.create(
                food_name=serialized.data['food_name'],
                description=serialized.data['description'],
                address=serialized.data['address'],
            )
            order.save()
            return Response(str('message: order created'), status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


######################### DELETE order BY ID #####################################

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny, ])
def delete_order_by_id(request):
    try:
        order_id = request.GET.get('order_id')
        try:
            order = Order.objects.get(id=order_id)
        except Exception:
            return Response({'Fail': "order by this id does not exist"}, status=status.HTTP_404_NOT_FOUND)
        order.delete()

        return Response(
            {'Success': 'order deleted'},
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'Something went wrong deleting order'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
