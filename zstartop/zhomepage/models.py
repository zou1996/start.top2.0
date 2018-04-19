from django.db import models


# Create your models here.

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class People(models.Model):
    name = models.CharField(null=True,blank=True,max_length=20)
    def __str__(self):
        return self.name

class Article(models.Model):
    headline = models.CharField(null=True,blank=True,max_length=50)
    content = models.TextField(null=True,blank=True,max_length=2000)
    TAG_CHOICES = (
        ('Coding Life',(
                    ('django','Django'),
                    ('scrapy','Scrapy'),
                )
        ),
        ('Enjoy Life',(
                    ('hangzhou','Hangzhou'),
                    ('wenzhou','Wenzhou'),
                )
        ),
    )
    tag = models.CharField(null=True,blank=True,max_length=20,choices=TAG_CHOICES)
    def __str__(self):
        return self.headline

class Comment(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    comment = models.TextField()
    belong_to = models.ForeignKey(to=Article, related_name='under_comments', null=True, blank=True,on_delete=models.CASCADE)
    best_comment = models.BooleanField(default=False)
    def __str__(self):
        return self.comment
