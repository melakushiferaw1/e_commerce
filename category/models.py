from django.db import models
from django.urls import reverse
#first models of project 3A
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=20, blank=True)
    category_images = models.ImageField(upload_to='categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
    def __str__(self):
        return self.category_name