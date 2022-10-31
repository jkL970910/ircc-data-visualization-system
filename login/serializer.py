from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import UserProfile

class LoginWithToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print('test:data', user)
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...
        return token

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserProfile
        fields = (
            'user_id', 
            'full_name', 
            'user_name', 
            'user_password', 
            'user_password2', 
            'user_gender', 
            'user_birthdate'
        )

    # def validate(self, attrs):
    #     if attrs['user_password'] != attrs['user_password2']:
    #         raise serializers.ValidationError(
    #             {"password": "Password fields didn't match."})

    #     return attrs

    # def create(self, validated_data):
    #     user = UserProfile.objects.create(
    #         user_id=validated_data['user_id'],
    #         full_name=validated_data['full_name'],
    #         user_name=validated_data['user_name'],
    #         user_gender=validated_data['user_gender'],
    #         user_birthdate=validated_data['user_birthdate']
    #     )

    #     user.set_password(validated_data['user_password'])
    #     user.save()

    #     return user
