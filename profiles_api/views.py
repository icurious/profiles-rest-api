from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
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


class HelloViewSets(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializers

    def list(self,request):
        a_list = [
            'This is viewset',
            'This is list'
        ]

        return Response({'message': 'hello', 'list': a_list})
    
    def create(self,request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        name = serializer.validated_data.get('name')

        message = 'Hello {}'.format(name)

        return Response({'message': message})
    
    def retrieve(self,request,pk=None):
        return Response({'http': 'GET'})

    def update(self,request,pk=None):
        return Response({'http': 'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http': 'PATCH'})

    def delete(self,request,pk=None):
        return Response({'http': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES