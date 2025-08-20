from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Gene
from .serializers import GeneSerializer


class CustomGenePagination(PageNumberPagination):
    page_size_query_param = "pagesize"

    def get_paginated_response(self, data):
        return Response(
            {
                "items": data,
                "pagination": {
                    "current_item_count": len(data),
                    "current_page_number": self.page.number,
                    "pagination_size": self.page_size,
                    "total_item_count": self.page.paginator.count,
                    "total_page_count": self.page.paginator.num_pages,
                },
            }
        )


class GeneViewSet(viewsets.ModelViewSet):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer
    pagination_class = CustomGenePagination
