from django.contrib import admin
from .models import Course, Category
# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "date", "available");
    list_filter = ("available",);
    search_fields = ("title", "description", "date");
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",  ) }