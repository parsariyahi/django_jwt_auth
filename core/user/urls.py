from django.urls import path

from user.api.user import Usertest

urlpatterns = [
    path('', Usertest.as_view()),
]