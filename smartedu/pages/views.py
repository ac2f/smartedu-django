from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'index.html');
def about(request):
    return render(request, 'about.html');
def courses(request):
    # if (int(id)>1):
    #     return render(request, f'course-grid-{id}.html');
    # return redirect("/courses/2");
    return render(request, f"course-grid-4.html");
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
