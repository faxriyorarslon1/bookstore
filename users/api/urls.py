from django.urls import path, re_path
from .views import UserView, RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view({'post' : 'create'})),
    re_path(r'^(?P<pk>\d+)/user/$', UserView.as_view({'post' : 'create'}), name="user_view"),
]