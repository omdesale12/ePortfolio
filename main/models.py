from django.db import models
from user.models import UserProfile

# Create your models here.
class portfolio(models.Model):
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_created=True)
    description=models.TextField()

    def __str__(self):
        return str(self.user)