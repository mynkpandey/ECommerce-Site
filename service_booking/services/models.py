from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="FontAwesome icon class", default="fas fa-concierge-bell")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='services')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")
    provider = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name