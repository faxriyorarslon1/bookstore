from users.models import CustomUser as User
from rest_framework import serializers
from django.contrib.auth import password_validation
from django.core.validators import validate_email as email_validator
from django.core.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only': True}}
        
    def create(self, validated_data):
        return User.objects.create_user(validated_data['username'],
                                        validated_data['email'], 
                                        validated_data['password'])
    
    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def validate_email(self, value):
        email_validator(value)
        return value
    
    def validate_username(self, value):
        # for some reason User object of the django doesn't raise a validation error
        # when the length of the username is less than 8? so raise it manually
        if len(value) >= 8:
            return value 
        else:
            raise ValidationError(message="Username length must be greater than 7", code=400)
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        
    def update(self, instance, validated_data):
        password = validated_data.get('password', instance.password)
        instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)        