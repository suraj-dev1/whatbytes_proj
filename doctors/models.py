from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # creator or owner
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.specialization}"
