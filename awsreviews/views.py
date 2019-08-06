from django.http import HttpResponse
from django.shortcuts import render
import json
import urllib.request
from urllib.request import urlopen

from django.shortcuts import render, get_object_or_404
from .forms import SearchForm
from django.shortcuts import redirect

def index(request):
    return render(request, 'awsreviews/index.html')

# Create your views here.
def search_result(request):

    if request.method == "GET":
        form=SearchForm(request.GET)
        if form.is_valid():
            search = form.save(commit=False)
            search_query=search.query 

            #URL='http://ec2-3-17-27-254.us-east-2.compute.amazonaws.com:8983/solr/reviews/select?q=*%3A*&rows=0&&facet=true&facet.pivot=product_id,star_rating&facet.limit=10&wt=json'
            URL='http://ec2-3-17-27-254.us-east-2.compute.amazonaws.com:8983/solr/reviews/select?wt=json&'+search_query
            response = urlopen(URL)
            string = response.read().decode('utf-8')
            json_obj = json.loads(string)
            return HttpResponse(json.dumps(json_obj),content_type="application/json")
            #return render(request, 'awsreviews/search_result.html', {'search_result':json_obj })
    else:
       return render(request, 'awsreviews/index.html')

