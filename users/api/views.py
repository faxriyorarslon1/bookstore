# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import RegisterSerializer, UserSerializer
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = UserSerializer
    pagination_class = None
    
    def get_queryset(self):
        return User.objects.all().filter(pk=self.request.user.id)

class RegisterView(viewsets.ModelViewSet):
   serializer_class = RegisterSerializer
   get_queryset = User.objects.all()
   permission_classes = (AllowAny,)

   def create(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       user = serializer.save()
       payload = jwt_payload_handler(user)
       token = jwt_encode_handler(payload)
       return Response(
           data={
               "user": UserSerializer(user,context=self.get_serializer_context()).data,
               "token" : token
               })