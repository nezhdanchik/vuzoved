from django.urls import path

from . import views

urlpatterns = [
    path("login/<return_url>/", views.login_user, name="login"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("tst/<t>/", views.tst, name="tst"),
    path("tst/", views.tst, name="tst"),
]