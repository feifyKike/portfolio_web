from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    """About Page Text"""
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Displaying a string representation"""
        return str(self.created_on)