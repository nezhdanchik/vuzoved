from django.urls import path

from . import views

# app_name = 'vuz'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("university/<slug:slug_university>/feedback/", views.FeedbackView.as_view(), name="feedback"),
    path("university/<slug:slug_university>/", views.UniversityView.as_view(), name="university"),
    path("about/", views.AboutView.as_view(), name="about"),
]