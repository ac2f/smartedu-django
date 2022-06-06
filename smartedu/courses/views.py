from django.shortcuts import render
from .models import Course
from colorama import Fore, init
import json
init(convert=True, autoreset=True)  
# Create your views here.
def index(request, id:str=""):
    data = [{"title": course.title, "description": course.description, "image":course.image, "date": course.date, "available": course.available, "href": str(course.id)} for course in Course.objects.all()];
    print(Fore.LIGHTBLUE_EX, str(data));
    return render(request, "course-grid-4.html", {"courses": data})