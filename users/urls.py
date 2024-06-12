from django.urls import path
from .views import RegisterView,UserDetailView,UserLoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('users/', RegisterView.as_view(), name='user-create'),
    path('users/profile/', UserDetailView.as_view(), name='user-detail'),
    path('users/login/', UserLoginView.as_view(), name='user-login'),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]