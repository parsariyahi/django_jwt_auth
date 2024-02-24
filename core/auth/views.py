from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from auth.permissions import AdminOnlyPermission

class TokenVerify(APIView):
    """is Token Valid or Not

    Args:
        APIView (_type_): _description_

    Returns:
        _type_: _description_
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # print(request.headers)
        return Response({"vlid": True})