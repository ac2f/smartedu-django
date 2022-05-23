from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
# Create your views here.
def index(request):
    return render(request, 'index.html');
def about(request):
    return render(request, 'about.html');

def blog(request):
    return render(request, 'blog.html');
def blog_single(request):
    return render(request, 'blog-single.html');
def teachers(request):
    return render(request, 'teachers.html');
def pricing(request):
    return render(request, 'pricing.html');
def contact(request):
    return render(request, 'contact.html');
