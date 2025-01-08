from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    metadata = models.JSONField()
    def __str__(self):
        return self.subcategory