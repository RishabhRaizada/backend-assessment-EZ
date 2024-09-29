from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.core.exceptions import ValidationError

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ops', 'Ops User'),
        ('client', 'Client User'),
    )
    role = models.CharField(max_length=6, choices=ROLE_CHOICES)

  
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='custom_user',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user_permission',
    )

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')

    def clean(self):
        extension = os.path.splitext(self.file.name)[1]
        if extension not in ['.pptx', '.docx', '.xlsx']:
            raise ValidationError('Invalid file type. Only .pptx, .docx, .xlsx allowed.')

    def __str__(self):
        return self.file.name
