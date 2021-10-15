from users.models import CustomUser as User
from rest_framework import serializers
from .models import AuthorModel, BookModel, BookRatingModel, CategoryModel, PublisherModel, BaseModel
from django.contrib.auth import password_validation
from django.core.validators import validate_email as email_validator
from django.core.exceptions import ValidationError 
from users.serializers import UserSerializer
            
class LibraryBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        exclude = ('is_test_data', 'created_at', 'modified_at', 'created_by', 
                   'modified_by', 'deleted_at', 'deleted_by')
        depth = 1

class AuthorSerializer(LibraryBaseSerializer):
    class Meta(LibraryBaseSerializer.Meta):
        model = AuthorModel
        
class CategorySerializer(LibraryBaseSerializer):
    class Meta(LibraryBaseSerializer.Meta):
        model = CategoryModel

class PublisherSerializer(LibraryBaseSerializer):
    class Meta(LibraryBaseSerializer.Meta):
        model = PublisherModel

class BookRatingSerializer(LibraryBaseSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta(LibraryBaseSerializer.Meta):
        model = BookRatingModel
        depth = 0

class BookSerializer(LibraryBaseSerializer):
    # adding serializers manually ensured that base serializer is being called on each request,
    # otherwise every data about the foreign keys are shown
    # this way exclude field on the base is obeyed
    author = AuthorSerializer(many=False, read_only=True) 
    category = CategorySerializer(many=False, read_only=True)
    publisher = PublisherSerializer(many=False, read_only=True)
    rating = serializers.ReadOnlyField(source='overall_rating')

    class Meta(LibraryBaseSerializer.Meta):
        model = BookModel
