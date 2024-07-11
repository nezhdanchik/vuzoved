from django.urls import path

from . import views

urlpatterns = [
    path("login/<return_url>/", views.LoginUser.as_view(), name="login"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("register/success/", views.RegisterSuccessView.as_view(), name="register_success")
]