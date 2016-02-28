from django.db import models

# Create your models here.
class SingUp(models.Model):
    email = models.EmailField(max_length=254)
    full_name = models.CharField(max_length=120, default='', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.email
