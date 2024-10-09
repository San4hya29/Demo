from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Appointment(models.Model):
    TEST_CHOICES = [
        ('test1', 'Test 1'),
        ('test2', 'Test 2'),
        # Add more test types as needed
    ]

    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    test_type = models.CharField(max_length=10, choices=TEST_CHOICES)
    date = models.DateField(validators=[MinValueValidator(limit_value=timezone.now().date())])
    timing = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.test_type}"

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    file_upload = models.FileField(upload_to='uploads/', blank=True, null=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('recived', 'Recived'),
        
    ]
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.user.username
    
