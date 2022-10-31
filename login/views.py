from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from django.http import JsonResponse
from .serializer import LoginWithToken, UserProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from .models import UserProfile
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

class LoginWithToken(TokenObtainPairView):
    serializer_class = LoginWithToken

class RegisterView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/login/token/',
        '/login/register/',
        '/login/token/refresh/'
    ]
    return Response(routes)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_list(request):
    # GET list of Users, POST a new user, DELETE all
    if request.method == 'GET':
        users = UserProfile.objects.all()

        user_profile_serializer = UserProfileSerializer(users, many=True)
        return JsonResponse(user_profile_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_profile_serializer = UserProfileSerializer(data=user_data)
        if user_profile_serializer.is_valid():
            user_profile_serializer.save()
            return JsonResponse(user_profile_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_profile_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        users.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    try: 
        userProfile = UserProfile.objects.get(pk=pk) 
    except UserProfile.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    # GET, Update, Delete user by id
    if request.method == 'GET':
        user_profile_serializer = UserProfileSerializer(userProfile)
        return JsonResponse(user_profile_serializer.data)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_profile_serializer = UserProfileSerializer(user_data, data=user_data)
        if user_profile_serializer.is_valid():
            user_profile_serializer.save()
            return JsonResponse(user_profile_serializer.data)
        return JsonResponse(user_profile_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = UserProfile.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

