from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

# Create your views here.


class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializers

    def get(self,request,format=None):
        an_api = [
            'This is GET',
            'This is http method'
        ]

        return Response({'message':'hello','api_view':an_api})

    def post(self,request):
        serializer = self.serializer_class(data = request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        name = serializer.validated_data.get('name')

        message = 'Hello {}'.format(name)

        return Response({'message': message})
    
    def put(self,request,pk=None):
        return Response({'message': 'PUT'})

    def patch(self,request,pk=None):
        return Response({'message': 'PATCH'})

    def delete(self,request,pk=None):
        return Response({'message': 'DELETE'})