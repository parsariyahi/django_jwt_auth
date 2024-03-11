from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from auth.permissions import AdminOnlyPermission


class TokenObtain(TokenObtainPairView):

    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)
        ref_token = response.data["refresh"]
        response.set_cookie("refresh", ref_token, httponly=True, secure=False)

        return response


class TokenVerify(APIView):
    """is Token Valid or Not

    Args:
        APIView (_type_): _description_

    Returns:
        _type_: _description_
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        resp = Response({"vlid": True})
        return resp


class RefreshToken(TokenRefreshView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        request.data["refresh"] = request.COOKIES["refresh"]
        return super().post(request, *args, **kwargs)


class BlacklistToken(TokenBlacklistView):
    def post(self, request: Request, *args, **kwargs):
        ref_token = request.COOKIES.get("refresh", None)
        request.data["refresh"] = ref_token
        response = super().post(request, *args, **kwargs)

        return response