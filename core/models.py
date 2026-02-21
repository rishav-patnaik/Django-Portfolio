from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Certification(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    credential_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Milestone(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    year = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title