from django.shortcuts import render
from .models import Search
import json

# Create your views here.
def search_list(request):

    search_result=list(Search.objects.all())[0]
	
    return render(request, 'awsreviews/search_list.html', {'search_result':search_result })
