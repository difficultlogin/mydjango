from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_desc = models.TextField()

class Post(models.Model):
    post_name = models.CharField(max_length=255)
    post_date = models.DateField(auto_now=True)
    post_category = models.ForeignKey(Category)
    post_body = models.TextField()