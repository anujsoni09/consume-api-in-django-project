from django.shortcuts import render


from django.shortcuts import render
from django.http import HttpResponse
import requests
def posts(request):
    
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    posts = response.json()
    
    return render(request, "posts.html" ,{'posts': posts})
    pass