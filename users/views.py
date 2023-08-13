from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import WallUser
from .serializers import TokenJWTSerializer, RegisterSerializer


class TokenJWTView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenJWTSerializer


class RegisterView(generics.CreateAPIView):
    queryset = WallUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
