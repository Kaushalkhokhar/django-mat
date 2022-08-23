from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    '''Custom User Model'''

    name = models.Charfield(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(max_length=18, null=True, blank=True)
    gender = models.CharField(choices=GenderChoices, 
        max_length=200, 
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(default=False)
    ceated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def save(self, *args, **kwargs):
        if not self.updated_at:
            self.updated_at = datetime.datetime.now()
        super().save(*args, **kwargs)
        
    def __str__(self):
        if self.name:
            return f'{str(self.name).title()'
        else:
            return f'{self.email}'
