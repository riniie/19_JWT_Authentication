from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView
from api.views import StudentModelViewSet

router = DefaultRouter()
router.register('student', StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest', include('rest_framework.urls')),
    path('', include(router.urls)),

    path('gettoken/', TokenObtainPairView.as_view(), name='get_token'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verify_token'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refresh_token'),
]
