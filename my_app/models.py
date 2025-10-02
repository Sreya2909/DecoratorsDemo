# Create your models here.
from django.db import models 

from django.contrib.auth.models import User 

 

class UserProfile(models.Model): 

    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    bio = models.TextField() 

 

    class Meta: 

        permissions = [ 

            ("can_add_user", "Can add a new user to the system"), 

        ] 