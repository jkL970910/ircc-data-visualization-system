from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializerLogin(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["user_id", "username", "first_name", "last_name", "email", "is_staff", "full_name", "user_gender", "user_birthdate", "user_address", "user_phone", "user_icon", "user_postcode",]

class UserProfileSerializerInfo(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["username", "email", "is_staff", "full_name", "user_gender", "user_birthdate", "user_address", "user_phone", "user_postcode"]