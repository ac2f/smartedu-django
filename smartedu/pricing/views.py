from django.shortcuts import render
from .models import Pricing
# Create your views here.
def index(request):
    data = Pricing.objects.all().values().__dict__;
    data["rows"] = data["rows"].split("{{n}}")
    return render(request, 'pricing.html', {"prices"});