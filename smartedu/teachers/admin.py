from django.contrib import admin
from .models import Teacher
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "jobTitle", "registerDate");
    # list_filter = ("available",);
    search_fields = ("firstName", "lastName", "jobTitle");
