from django.shortcuts import render

# Create your views here.
def query_list(request):
    return render(request, 'awsreviews/query_list.html', {})
