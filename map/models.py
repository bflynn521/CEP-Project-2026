from django.db import models

# Create your models here.

class User(models.Model):
    name        = models.CharField(max_length=100)
    location    = models.CharField(max_length=200)
    image_1     = models.ImageField(upload_to='media/profile/', blank=True, null=True)
    image_2     = models.ImageField(upload_to='media/car/',     blank=True, null=True)
    description = models.TextField(blank=True)
    seats_available = models.PositiveSmallIntegerField(default=3)
    departure_time  = models.TimeField(blank=True, null=True)
    phone           = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
 
    def __str__(self):
        return f"{self.name} — {self.location}"