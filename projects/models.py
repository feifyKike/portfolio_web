from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Technology(models.Model):
    """Showing a technology used in project"""
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Technologies'

    def __str__(self):
        """Displaying a string representation"""
        return self.name

class Project(models.Model):
    """Showing the recent projects"""
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=300, default="Follow the link above to the blog post.")
    description = RichTextField(blank=True, null=True)
    technology = models.ManyToManyField('Technology', related_name='projects')
    link = models.URLField(max_length=500)
    anotherlink = models.URLField(max_length=500, default="", blank=True)
    videodemo = models.URLField(max_length=600, default="", blank=True)

    class Meta():
        verbose_name_plural = 'Projects'

    def __str__(self):
        """Returning a string representation"""
        return self.title

    def aslist(self):
        return self.technology.split(", ")