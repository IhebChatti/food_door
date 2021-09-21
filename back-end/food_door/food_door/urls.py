"""food_door URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from users import views as  user_views
from restaurant import views as r_views
from products import views as food_views
from orders import views as order_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    ######################### User Url's #####################################
    
    path('signup/', user_views.create_user),
    path('list_users', user_views.list_users),
    path('get_user', user_views.get_user_by_id),
    path('delete_user', user_views.delete_user_by_id),
    
    ######################### Restaurant Url's #####################################
    
    path('list_restaurants', r_views.list_restaurants),
    path('get_restaurant', r_views.get_restaurant_by_id),
    path('create_restaurant', r_views.create_restaurant),
    path('restaurant_image', r_views.ImageViewSet.as_view(), name='restaurant_image'),
    path('delete_restaurant', r_views.delete_restaurant_by_id, name='delete_restaurant'),
    
    ######################### Food Url's #####################################
    
    path('list_food', food_views.list_food),
    path('get_food', food_views.get_food_by_id),
    path('create_food', food_views.create_food),
    path('delete_food', food_views.delete_food_by_id, name='delete_food'),
    path('food_image', food_views.ImageViewSetFood.as_view(), name='food_image'),
    
    ######################### Food Url's #####################################
    
    path('list_orders', order_views.list_orders),
    path('get_order', order_views.get_order_by_id),
    path('create_order', order_views.create_order),
    path('delete_order', order_views.delete_order_by_id, name='delete_food'),
    ############################ AUTH ######################################
    # re_path(r'jwt/obtain/$', user_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', user_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]
