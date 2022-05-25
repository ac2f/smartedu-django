from django.shortcuts import render
from .models import Teacher
# Create your views here.
def index(request):
    return render(request, "teachers.html", {"teachers": Teacher.objects.all().values()});