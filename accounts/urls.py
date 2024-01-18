# accounts/urls.py
from django.urls import path

from .views import SignUpView, student

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("student/", student, name="student"),
]