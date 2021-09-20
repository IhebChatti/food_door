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


######################### LIST USERS #####################################

@api_view(['GET'])
@permission_classes([permissions.AllowAny, ])
def list_users(request):
    try:
        _users = User.objects.all()
        serializer = UserSerializer(_users, many=True)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'no users'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

######################### LIST USER BY ID #####################################

@api_view(['GET'])
@permission_classes([permissions.AllowAny, ])
def get_user_by_id(request):
    try:
        user_id = request.GET.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except:
            return Response({'Error', 'No user found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'Internal server error'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


######################### DELETE USER BY ID #####################################

@api_view(['DELETE'])
@permission_classes([permissions.AllowAny, ])
def delete_user_by_id(request):
    try:
        user_id = request.GET.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except Exception:
            return Response({'Fail': "User by this id does not exist"}, status=status.HTTP_404_NOT_FOUND)

        user.delete()

        return Response(
            {'Success': 'user deleted'},
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'Something went wrong deleting user'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
