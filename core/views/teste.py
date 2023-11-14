from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Teste
from core.serializers import TesteSerializer


class TesteViewSet(ModelViewSet):
    queryset = Teste.objects.all()
    serializer_class = TesteSerializer