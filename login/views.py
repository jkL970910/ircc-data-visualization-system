from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.parsers import JSONParser 
from django.http import JsonResponse
from .serializer import MyTokenObtainPairSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from .models import UserProfile
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def check_login(request):
    username = request.POST.get('user_name', None)
    password = request.POST.get('pass_word', None)
    if username and password:
        username = username.strip()
        try:
            user = UserProfile.objects.get(user_name=username)
        except:
            return JsonResponse({'message': 'No Such User Name!'}, status=status.HTTP_400_BAD_REQUEST)
        if user.user_password == password:
            user_profile_serializer = UserProfileSerializer(user)
            return JsonResponse(user_profile_serializer.data)
        else:
            return JsonResponse({'message': 'Password Didnt Match!'}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'message': 'Username or Password can not be empty!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
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
            if (UserProfile.objects.filter(user_name=user_data["user_name"]).exists()):
                return JsonResponse({'message': 'Username Already Existed!'}, status=status.HTTP_400_BAD_REQUEST)
            user_profile_serializer.save()
            return JsonResponse(user_profile_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_profile_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        users.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, user_id):
    try: 
        userProfile = UserProfile.objects.get(user_id=user_id) 
    except UserProfile.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    # GET, Update, Delete user by id
    if request.method == 'GET':
        user_profile_serializer = UserProfileSerializer(userProfile)
        return JsonResponse(user_profile_serializer.data)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_profile_serializer = UserProfileSerializer(data=user_data)
        if user_profile_serializer.is_valid():
            user_profile_serializer.save()
            return JsonResponse({'message': '{} User were updated successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse(user_profile_serializer.validated_data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = UserProfile.objects.all().delete()
        return JsonResponse({'message': '{} User were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

