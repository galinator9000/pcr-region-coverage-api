from django.http import HttpResponse
from rest_framework import viewsets
from .models import Gene
from .serializers import GeneSerializer


class GeneViewSet(viewsets.ModelViewSet):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer
