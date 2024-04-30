from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
