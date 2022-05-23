from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader, render

def index(request):
    return render(request, 'index.html');
    return HttpResponse(loader.get_template("index.html").render());