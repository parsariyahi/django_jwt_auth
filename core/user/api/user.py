from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

class Usertest(APIView):
    """is Token Valid or Not

    Args:
        APIView (_type_): _description_

    Returns:
        _type_: _description_
    """

    def get(self, request, format=None):
        # print("Verify Token")
        # print("headers \n", request.headers)
        resp = Response({"vlid": True})
        return resp