from django.db import models



class Student(models.Model):
    student_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    course_grades = models.JSONField()  # Stores all course details dynamically
    batch = models.CharField(max_length=10, db_index=True, default="")  # New field for batch

    def __str__(self):
        return f"{self.name} ({self.student_id})"
