from django.urls import path

from . import views

# app_name = 'vuz'

urlpatterns = [
    path("", views.index, name="index"),
    path("university/<slug:slug_university>/", views.university, name="university", ),
    path("about/", views.about, name="about"),
    path("name/", views.get_name, name="name"),
]