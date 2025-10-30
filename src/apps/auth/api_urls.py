from django.urls import path, register_converter, include
from rest_framework import routers
from .api_views import (
    RegistrarUsuarioViewSet, PasswordResetRequestView, PasswordResetConfirmView,me
)

router = routers.DefaultRouter()
router.register(r'register', RegistrarUsuarioViewSet, basename='register')

urlpatterns = [
    path('auth/', include(router.urls)),
    path('auth/password-reset/', PasswordResetRequestView.as_view({'post': 'create'}), name='password_reset'),
    path('auth/password-reset-confirm/', PasswordResetConfirmView.as_view({'post': 'create'}), name='password_reset_confirm'),
    path('auth/api/me/', me, name='me'),
]