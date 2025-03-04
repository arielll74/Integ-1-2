from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length =255)
    content = models.TextField(blank=True, null=True, default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.TextField(blank=False, null=False, default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

