

from django.db import models

class Resume(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    education = models.TextField()
    work_experience = models.TextField()
    skills = models.TextField()
    # Add more fields as needed

    def __str__(self):
        return self.full_name
