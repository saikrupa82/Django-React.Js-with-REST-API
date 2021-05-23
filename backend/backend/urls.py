from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from API import views

router = routers.DefaultRouter()
router.register(r'APIs', views.APIView, 'API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]