# Generated by Django 5.0 on 2023-12-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_student_current_status_student_gender_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="phone_number",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
