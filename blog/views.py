from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#creating request handler

def post_list(request):
    #return HttpResponse('Hello worldddddk')
    return render(request, 'blog/post_list.html', {})

def index(request):
    return render(request, 'blog/index.html', {})

def shopDeatil(request):
    return render(request, 'blog/shop-detail.html', {})

def shopListing(request):
    return render(request, 'blog/shop-listing.html', {})


def home(request):
    return HttpResponse('Shout out to Hiit students')

