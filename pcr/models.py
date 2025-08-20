from django.db import models


class Gene(models.Model):
    name = models.CharField(max_length=200)
    unique_gene_ids = models.JSONField()
    chromosome = models.CharField(max_length=10)
    start = models.IntegerField()
    end = models.IntegerField()
    primer_based_count = models.IntegerField()
    percentage = models.FloatField()
    minimum_count = models.IntegerField()
    maximum_count = models.IntegerField()
    forward_count = models.IntegerField()
    reverse_count = models.IntegerField()
    meandepth = models.FloatField()
    stdev = models.FloatField(null=True)
