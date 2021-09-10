from django.urls import path, include
from rest_framework import routers
from . import views

# URL config using DefaultRouter
router = routers.DefaultRouter()

# registering our patterns


urlpatterns = [
    path('', include(router.urls)),
]
