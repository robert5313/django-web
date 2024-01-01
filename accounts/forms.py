from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Student
from .models import User
from django import forms

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")


class UserChangeForm(UserChangeForm):
    
        class Meta:
            model = User
            fields = ("username", "email")

class StudentForm(forms.ModelForm):
     class Meta:
        model = Student
        fields = (
            "roll_no",
            "course",
            "year",
            "section",
            "phone_number",
            "city",
            "country",
            "image",
        )
     