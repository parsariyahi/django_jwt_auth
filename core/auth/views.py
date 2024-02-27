from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth.permissions import AdminOnlyPermission


class TokenObtain(TokenObtainPairView):

    def post(self, request: Request, *args, **kwargs) -> Response:
        # print("Token Obtain")
        response = super().post(request, *args, **kwargs)
        ref_token = response.data["refresh"]
        response.set_cookie("refresh", ref_token, httponly=True, secure=False)
        # print("response cookies\n", response.cookies)
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
        # print("Verify Token")
        # print("headers \n", request.headers)
        resp = Response({"vlid": True})
        return resp

class RefreshToken(TokenRefreshView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        # print("Refresh Token")
        # print("headers \n", request.headers)
        # print("data \n", request.data)
        # print("cookies \n", request.COOKIES)
        request.data["refresh"] = request.COOKIES["refresh"]
        # print("data \n", request.data)
        return super().post(request, *args, **kwargs)