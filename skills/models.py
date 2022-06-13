from django.db import models

# Create your models here.


class Skill(models.Model):
    RATINGS = [
        (0, "0"),
        (10, "1"),
        (20, "2"),
        (30, "3"),
        (40, "4"),
        (50, "5"),
        (60, "6"),
        (70, "7"),
        (80, "8"),
        (90, "9"),
        (100, "10")
    ]
    skill_name = models.CharField(max_length=50)
    skill_level = models.IntegerField(
        choices=RATINGS,
        default=0
    )

    class Meta():
        verbose_name_plural = 'Skills'

    def __str__(self):
        """Returning a string representation"""
        return self.skill_name

class ByCategory(models.Model):
    category = models.CharField(max_length=200)
    string_list = models.CharField(max_length=800)

    class Meta():
        verbose_name_plural = "ByCategories"

    def __str__(self):
        """Return a string representation"""
        return self.category
        
    def string_aslist(self):
        return self.string_list.split(",")

class Experience(models.Model):
    experience = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    description = models.TextField(max_length=400)

    class Meta():
        verbose_name_plural = "Experiences"

    def __str__(self):
        """Return a string representation"""
        return self.experience