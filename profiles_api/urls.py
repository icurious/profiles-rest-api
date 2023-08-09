from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views 

router = DefaultRouter()
router.register('hellow-viewset', views.HelloViewSets, base_name = 'hello-viewset')

urlpatterns = [
    path('hellow-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))

]