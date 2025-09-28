from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ("faculty", "Faculty"),
        ("course_coordinator", "Course Coordinator"),
        ("module_coordinator", "Module Coordinator"),
        ("pac", "PAC"),
        ("dfb", "DFB"),
        ("cdc", "CDC"),
    ]
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default="faculty")

class MoM(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    agenda = models.TextField()
    discussion = models.TextField()
    action_items = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} ({self.date})"

