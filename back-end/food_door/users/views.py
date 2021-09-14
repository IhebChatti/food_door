from django.shortcuts import render
from users.models import User
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from users.serializers import UserSerializer
from rest_framework import status


@api_view(['POST', 'GET'])
@permission_classes([permissions.AllowAny, ])
def create_user(request):
    try:
        user_data = request.data
        serialized = UserSerializer(data=user_data)
        breakpoint()
        if serialized.is_valid():
            user = User.objects.create(
                email=serialized.data['email'],
                password=serialized.data['password'],
                first_name=serialized.data['first_name'],
                last_name=serialized.data['last_name'],
                address=serialized.data['address'],
                phone=serialized.data['phone'],
            )
            user.save()
            return Response({'message': 'created'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
