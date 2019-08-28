from django.http import HttpResponse
from django.shortcuts import render
import json
import urllib.request
from urllib.request import urlopen
import urllib.parse

from django.shortcuts import render, get_object_or_404
from .forms import SearchForm
from .forms import StreamForm
from django.shortcuts import redirect



def index(request):
    return render(request, 'awsreviews/index.html')

def search(request):
    return render(request, 'awsreviews/search.html')

def contact(request):
    return render(request, 'awsreviews/contact.html')

def about(request):
    return render(request, 'awsreviews/about.html')

# Create your views here.
def search_result(request):

    if request.method == "GET":
        form=SearchForm(request.GET)
        if form.is_valid():
            search = form.save(commit=False)
            search_query=search.query.replace(' ', '%20')
            
            #search_query=urllib.parse.quote(search.query)
            print (search_query)
            URL='http://ec2-3-17-27-254.us-east-2.compute.amazonaws.com:8983/solr/reviews/select?'+search_query
            response = urlopen(URL)
            string = response.read().decode('utf-8')
            json_obj = json.loads(string)
            return HttpResponse(json.dumps(json_obj),content_type="application/json")
            #return render(request, 'awsreviews/search_result.html', {'search_result':json_obj })
    else:
       return render(request, 'awsreviews/index.html')

def search_api(request):

    if request.method == "GET":
        form=SearchForm(request.GET)
        if form.is_valid():
            search = form.save(commit=False)
            search_query=search.query
            URL='http://ec2-3-17-27-254.us-east-2.compute.amazonaws.com:8983/solr/reviews/select?wt=xml&'+search_query
            print (URL)
            response = urlopen(URL)
            string = response.read().decode('utf-8')
            #json_obj = json.loads(string)
            return HttpResponse(string,content_type="application/xml")
            #return HttpResponse(json.dumps(json_obj),content_type="application/json")
            #return render(request, 'awsreviews/search_result.html', {'search_api":json_obj })
    else:
       return render(request, 'awsreviews/index.html')

def terms_result(request):

    if request.method == "GET":
        form=SearchForm(request.GET)
        if form.is_valid():
            search = form.save(commit=False)
            search_query=search.query 

            #URL='http://ec2-3-17-27-254.us-east-2.compute.amazonaws.com:8983/solr/reviews/select?q=*%3A*&rows=0&&facet=true&facet.pivot=product_id,star_rating&facet.limit=10'
            URL='http://ec2-3-17-27-254.us-east-2.compute.amazonaws.com:8983/solr/reviews/terms?'+search_query
            response = urlopen(URL)
            string = response.read().decode('utf-8')
            json_obj = json.loads(string)
            return HttpResponse(json.dumps(json_obj),content_type="application/json")
            #return render(request, 'awsreviews/terms_result.html', {'terms_result':json_obj })
    else:
       return render(request, 'awsreviews/index.html')

def stream_result(request):

    if request.method == "GET":
        form=StreamForm(request.GET)
        if form.is_valid():
            expr = form.save(commit=False)
            #expr_query=search.expr 
            expr_query=urllib.parse.quote(expr.expr)

            print (expr_query)
            #URL='http://ec2-3-17-27-254.us-east-2.compute.amazonaws.com:8983/solr/reviews/select?q=*%3A*&rows=0&&facet=true&facet.pivot=product_id,star_rating&facet.limit=10'
            
            URL='http://ec2-3-17-27-254.us-east-2.compute.amazonaws.com:8983/solr/reviews/stream?expr='+expr_query
            print (URL)
            response = urlopen(URL)
            string = response.read().decode('utf-8')
            json_obj = json.loads(string)
            return HttpResponse(json.dumps(json_obj),content_type="application/json")
            #return render(request, 'awsreviews/stream_result.html', {'stream_result':json_obj })
    else:
       return render(request, 'awsreviews/index.html')

