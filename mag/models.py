from django.db import models
from django.contrib.auth.models import User
class Categories(models.Model):
    class Meta():
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Contact(models.Model):
    class Meta():
        ordering = ['created_date']
    subject = models.CharField(max_length=100, null=True)
    sender = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.sender
class Posts(models.Model):
    def __str__(self):
        return f"{self.id} - {self.subject}"
    class Meta():
        verbose_name_plural = 'Posts'
        ordering = ['created_date']
    subject = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    category = models.ManyToManyField(Categories)
    images = models.ImageField(null=True)   
    views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)