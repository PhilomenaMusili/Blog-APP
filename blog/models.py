from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now, blank=True)
    category = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')

    def __str__(self):
        return self.title
