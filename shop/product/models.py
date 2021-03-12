from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField()  # @TODO implement


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)


class Tag(models.Model):
    title = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)
