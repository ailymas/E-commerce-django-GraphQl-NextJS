from distutils.command import upload
from itertools import product
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="SubCategories")
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="Products")
    subCategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name="Products")
    description=models.TextField()
    price=models.PositiveIntegerField()
    amount_in_Stock=models.PositiveIntegerField()
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image=models.ImageField(upload_to='productImages/')

class Rating(models.Model):
    product=models.ForeignKey(Product,related_name="rating",on_delete=models.CASCADE)
    stars=models.PositiveIntegerField()
    note=models.TextField()
    rating_from=models.ForeignKey(User,on_delete=models.CASCADE,related_name='ratingFrom')
    created_on= models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    product=models.ForeignKey(Product,related_name="comments",on_delete=models.CASCADE)
    comment_from=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_given')
    body=models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)


