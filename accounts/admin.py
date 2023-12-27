from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User, Student, Teacher, Subject, StudentSubject, TeacherSubject, Attendance, AttendanceRecord
# Register your models here.

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active',)

admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(StudentSubject)
admin.site.register(TeacherSubject)
admin.site.register(Attendance)
admin.site.register(AttendanceRecord)
