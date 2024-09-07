from django.db import models
from users.models import Profile

class Therapist(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=255)
    experience = models.IntegerField()

    def __str__(self):
        return self.profile.user.username