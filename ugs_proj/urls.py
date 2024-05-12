
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('ugs_app.urls')),
    path('admin/main', admin.site.urls),
    
    
   
]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
