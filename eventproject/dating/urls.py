from django.urls import path
from .import views


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login-view"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout-view"),
    path("dating/", views.dating, name="dating"),
    path("dashboard/", views.dashboard, name="dashboard")
]