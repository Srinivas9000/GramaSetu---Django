from django.urls import path
from .api_views import UserProfileAPIView


urlpatterns = [

    path(
        'profile/',
        UserProfileAPIView.as_view(),
        name='api-profile'
    ),

]