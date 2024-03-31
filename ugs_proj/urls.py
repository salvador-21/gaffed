
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', include('ugs_app.urls')),
    path('admin/', admin.site.urls),
   
]
