from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.

class Snack(models.Model):
    title = models.CharField(max_length=26)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,default=1)
    description = models.TextField()
    
    
    def __str__(self) -> str:
        return self.title
    
    #reverse to redirect
    def get_absolute_url(self):
        return reverse('snack_list')