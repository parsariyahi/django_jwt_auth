from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from auth.views import TokenVerify, RefreshToken, TokenObtain

urlpatterns = [
    path('', TokenVerify.as_view()),
    path('token/', TokenObtain.as_view(), name='token_obtain_pair'),
    path('token/refresh/', RefreshToken.as_view(), name='token_refresh'),
]