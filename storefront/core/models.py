from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
