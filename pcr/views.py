from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

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

    @action(detail=False, methods=["post"])
    def create_batch(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @action(detail=False, methods=["delete"])
    def delete_batch(self, request):
        ids_to_delete = request.data.get("ids", [])
        if not ids_to_delete:
            return Response(
                {"detail": "No IDs provided for deletion."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        genes_to_delete = Gene.objects.filter(id__in=ids_to_delete)
        if not genes_to_delete:
            return Response(
                {"detail": "No record found with the provided IDs."},
                status=status.HTTP_404_NOT_FOUND,
            )

        deleted_count, _ = genes_to_delete.delete()
        return Response(
            {"detail": f"{deleted_count} records deleted successfully."},
            status=status.HTTP_200_OK,
        )
