# students/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=120)
    dob = models.DateField(verbose_name="Date of birth")
    email = models.EmailField(unique=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    handled_by_teacher = models.BooleanField(
        default=False,
        help_text="Checked = teacher has reached out"
    )

    def __str__(self):
        return self.name
