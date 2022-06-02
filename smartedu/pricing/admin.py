from django.contrib import admin
from django.forms import ModelForm
from .models import Pricing
# Register your models here.
@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "price", "description", "rows");