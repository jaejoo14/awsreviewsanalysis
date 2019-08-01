from django.conf import settings
from django.db import models
from django.utils import timezone


class Search(models.Model):
    query = models.CharField(max_length=200)

    def __str__(self):
        return 'url'+self.query

