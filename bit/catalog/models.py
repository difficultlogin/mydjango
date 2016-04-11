from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_parent = models.ForeignKey('self', blank=True, null=True)
    category_desc = models.TextField(blank=True, null=True)
    category_img = models.ImageField(upload_to='static/upload')

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_category = models.ForeignKey(Category, blank=True, null=True)
    product_desc = models.TextField(blank=True, null=True)
    product_img = models.ImageField(upload_to='static/upload')

    def __str__(self):
        return self.product_name