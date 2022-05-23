from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("courses/", views.courses, name="courses"),
    path("blog/", views.about, name="blog"),
    path("teachers/", views.teachers, name="teachers"),
    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)