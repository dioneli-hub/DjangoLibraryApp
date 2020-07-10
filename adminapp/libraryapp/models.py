from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse('active', kwargs={'id': self.id})


class Book(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)


class BorrowTransaction(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=SET_NULL)
    is_returned = models.BooleanField(default='True')


