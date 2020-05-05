from django.db import models

# Create your models here.
"""
Author model:

Name (CharField)
Bio (TextField)

Recipe Model:

Title (CharField)
Author link -(ForeignKey)
Description (TextField)
Time Required (Charfield) (for example, "One hour")
Instructions (TextField)
"""


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    time = models.CharField(max_length=20)
    instructions = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

