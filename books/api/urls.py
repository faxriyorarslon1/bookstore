from django.urls import path, re_path
from .views import UserView, RegisterView


urlpatterns = [
    # path('register/', RegisterView.as_view(), name="user_register"),
    # re_path(r'^(?P<pk>\d+)/user/$', UserView.as_view(), name="user_view"),
]