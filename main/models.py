from django.db import models

class Documentary(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    # Add other fields as needed

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.name
