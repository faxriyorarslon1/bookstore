# books/models.py
import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Book(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=2000)
    cover = models.ImageField(upload_to='covers/',blank=True)

    class Meta: # new
        permissions = [
            ('special_status', 'Can read all books'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class Review(models.Model): # new
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews',)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.review        