from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from register.models import Register
from rest_api.serializers import RegisterSerializer


# Create your views here.


class RegisterModelViewSet(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
