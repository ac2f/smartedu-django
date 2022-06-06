from django.shortcuts import render
from .models import Pricing
import json
# Create your views here.
def index(request):
    data = [{"title":price.title, "subtitle":price.subtitle, "description": price.description, "price":price.price, "rows":price.rows.split("\\n")} for price in Pricing.objects.all()];
    return render(request, 'pricing.html', {"prices": data});