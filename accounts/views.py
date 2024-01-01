# accounts/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from accounts.models import Student
from accounts.forms import StudentForm


from .forms import UserCreationForm
from .models import Student

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        student = Student.objects.create(user=user)
        student.save()
        return super().form_valid(form)


def student_profile(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=request.user.student)
        if form.is_valid():
            form.save()
            return redirect("student_profile")