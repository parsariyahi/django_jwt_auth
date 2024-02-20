from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from auth.permissions import AdminOnlyPermission

class IsAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        print(request.COOKIES)
        return Response({"data": "some"})