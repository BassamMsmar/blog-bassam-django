from typing import ClassVar
from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.db.models.fields import TextField
from django.contrib.auth.models import User
from django.utils import  timezone
from django.urls import reverse



# Create your models here
class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='العنوان' )
    content = models.TextField(verbose_name='محتوى المقال')
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])

    class Meta():
        ordering =  ('-post_date', )

class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم' )
    email = models.EmailField(verbose_name='الايميل')
    body = models.TextField(max_length=500, verbose_name='نص التعليق ')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


    def __str__(self):
        return  'علق {} ' .format(self.name) 

    class Meta():
        ordering =  ('-comment_date', )

       