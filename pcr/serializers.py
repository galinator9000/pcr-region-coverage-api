from rest_framework import serializers
from .models import Gene


class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = [
            "id",
            "name",
            "unique_gene_ids",
            "chromosome",
            "start",
            "end",
            "primer_based_count",
            "percentage",
            "minimum_count",
            "maximum_count",
            "forward_count",
            "reverse_count",
            "meandepth",
            "stdev",
        ]

    def create(self, validated_data):
        return super().create(validated_data)
