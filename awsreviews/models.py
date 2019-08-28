from django.conf import settings
from django.db import models
from django.utils import timezone

import urllib.request
from urllib.request import urlopen
import json

class Search(models.Model):
    query= models.CharField(max_length=1000)

class Stream(models.Model):
    expr= models.CharField(max_length=1000)



