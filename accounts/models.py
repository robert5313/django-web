from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    is_staff = models.BooleanField('staff status', default=False)

    def __str__(self):
        return self.username
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    roll_no = models.CharField(max_length=10)
    course = models.CharField(max_length=10)
    year = models.IntegerField()
    section = models.CharField(max_length=1)
    def __str__(self):
        return self.user.username
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacher_id = models.CharField(max_length=10)
    def __str__(self):
        return self.user.username
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=20)
    subject_code = models.CharField(max_length=10)
    def __str__(self):
        return self.subject_name
    

class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.student.user.username + " " + self.subject.subject_name
    

class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.teacher.user.username + " " + self.subject.subject_name
    

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student.user.username + " " + self.subject.subject_name + " " + str(self.date)
    

class AttendanceRecord(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False) # True (Present) False (Absent)
    def __str__(self):
        return self.attendance.student.user.username + " " + self.attendance.subject.subject_name + " " + str(self.attendance.date) + " " + str(self.status)
    
class Assignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    assignment = models.FileField(upload_to='assignments/')
    def __str__(self):
        return self.teacher.user.username + " " + self.subject.subject_name + " " + str(self.date)
    

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission = models.FileField(upload_to='submissions/')
    def __str__(self):
        return self.assignment.teacher.user.username + " " + self.assignment.subject.subject_name + " " + str(self.assignment.date) + " " + self.student.user.username
    
class Notice(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    notice = models.CharField(max_length=100)
    def __str__(self):
        return self.teacher.user.username + " " + self.subject.subject_name + " " + str(self.date) + " " + self.notice

class StudentNotice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    def __str__(self):
        return self.student.user.username + " " + self.notice.teacher.user.username + " " + self.notice.subject.subject_name + " " + str(self.notice.date) + " " + self.notice.notice

class TeacherNotice(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.user.username} {self.notice.teacher.user.username} {self.notice.subject.subject_name} {self.notice.date} {self.notice.notice}"

class StudentMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.user.username} {self.subject.subject_name} {self.marks}"