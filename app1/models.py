from django.db import models
class Project(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    technologies = models.CharField(max_length=300)

    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

# Create your models here.
