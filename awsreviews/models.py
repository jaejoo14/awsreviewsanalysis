from django.conf import settings
from django.db import models
from django.utils import timezone

import urllib.request
from urllib.request import urlopen
import json


class Search(models.Model):
    #query_model = models.TextField()
    #query=str(query_model)

    query='q=*%3A*&rows=0&&facet=true&facet.pivot=product_id,star_rating&facet.limit=10'
    URL='http://ec2-18-223-160-8.us-east-2.compute.amazonaws.com:8983/solr/reviews/select?wt=json&'
    url_query=URL+query
    response = urlopen(url_query)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    json_str=json.dumps(json_obj)
     
    def publish(self):
        self.save()

    def __str__(self):
        return (self.json_str)

