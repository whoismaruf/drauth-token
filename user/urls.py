from django.urls import path, include
from user.views import check_token


urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('check/', check_token, name='check_token'),
]
