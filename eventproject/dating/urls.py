from django.urls import path
from .import views


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login-view"),
    path("logout/", views.logout_view, name="logout-view"),
    path("dashboard/", views.dashboard, name="dashboard")
]