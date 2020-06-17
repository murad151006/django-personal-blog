from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Blog(models.Model):
    slno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.CharField(max_length=100)
    posted = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title
    
class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE )
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.comment)