from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.views import RegisterView, TokenJWTView

urlpatterns = [
    path('login/', TokenJWTView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('register/', RegisterView.as_view(), name='register'),
]
