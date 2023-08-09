from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloApiView(APIView):

    def get(self,request,format=None):
        an_api = [
            'This is GET',
            'This is http method'
        ]

        return Response({'message':'hello','api_view':an_api})