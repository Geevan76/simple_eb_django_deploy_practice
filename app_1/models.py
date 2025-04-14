from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    profile_pic = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user.username}'s Profile"

