from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'apps'


class Blog_comment(models.Model):
    blog = models.ForeignKey('', models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Blog(models.Model):
    namde = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='image')


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', blank=True)

    class Post(models.Model):
        class Meta:
            app_label = 'apps'

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'product categories'

    def __str__(self):
        return self.name


class Product_list(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class Blog_category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
