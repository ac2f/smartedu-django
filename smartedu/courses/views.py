from django.shortcuts import render
from .models import Course
# Create your views here.
def courses (request):
    return render(request, "course-grid-4.html", {"courses": Course.objects.all().values()})