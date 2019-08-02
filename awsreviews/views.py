from django.shortcuts import render
from .models import Search
import json

# Create your views here.
def search_list(request):

    searchs=Search.objects.all()
	
    return render(request, 'awsreviews/search_list.html', {'searchs':searchs})
