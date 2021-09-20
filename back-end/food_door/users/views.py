from django.shortcuts import render
from users.models import User
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes, action
from users.serializers import UserSerializer
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

#     @action(detail=False, methods=['post'])
#     def post(self, request, *args, **kwargs):
#         breakpoint()
#         token = super().post(request, *args, **kwargs)
#         if token.data == {}:
#             resp = 'invalid_credentials'
#             return Response(resp, status=status.HTTP_400_BAD_REQUEST)
#         elif 'error' in token.data:
#             return Response(token.data, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return token


######################### CREATE USERS #####################################

@api_view(['POST'])
@permission_classes([permissions.AllowAny, ])
def create_user(request):
    try:
        user_data = request.data
        serialized = UserSerializer(data=user_data)
        breakpoint
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
            # return Response({'access': str(token.access_token), 'refresh': str(token), 'user': user_data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


######################### LIST USERS #####################################

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly, ])
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
        user.save()

        return Response(
            {'Success': 'user deleted'},
            status=status.HTTP_200_OK
        )
    except Exception:
        return Response(
            {'error': 'Something went wrong deleting user'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
