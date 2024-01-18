from rest_framework import serializers
from .models import User, Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")

class StudentSerializer(serializers.ModelSerializer):
    current_status = serializers.CharField(source="get_current_status_display")
    user = UserSerializer()
    gender = serializers.CharField(source="get_current_gender_display")
    roll_no = serializers.IntegerField()
    course = serializers.CharField(max_length=10, required=True)
    year = serializers.IntegerField()
    section = serializers.CharField(max_length=11, required=True)
    phone_number = serializers.IntegerField()
    city = serializers.CharField(max_length=20, required=True)
    country = serializers.CharField(max_length=20, required=True)
    image = serializers.ImageField()

    class Meta:
        model = Student
        fields = "__all__"