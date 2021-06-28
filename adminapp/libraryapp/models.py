from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_created_at(self):
        return f'{self.created_at.strftime("%d.%m.%Y")} в {self.created_at.strftime("%H:%M:%S")}'

    def get_updated_at(self):
        return f'{self.updated_at.strftime("%d.%m.%Y")} в {self.updated_at.strftime("%H:%M:%S")}'

    class Meta:
        abstract = True


class User(TimeStampMixin):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('active', kwargs={'id': self.id})


class Book(TimeStampMixin):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    remarks = models.TextField(max_length=500, default='no remarks', null=False)

    # book description select AVG (book_id)
    def get_average_grade(self):
        marks = Grade.objects.get(book_id=self.id)
        total = 0
        count = 0
        for grade in marks:
            if isinstance(grade, int):
                total += grade
                count += 1

        return round(total / count, 2)

    avg_grade = get_average_grade()


class BorrowTransaction(TimeStampMixin):
    user = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=SET_NULL)
    is_returned = models.BooleanField(default=True)


class Grade(TimeStampMixin):
    user = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=SET_NULL)

    AWFUL = 1
    BAD = 2
    OKAY = 3
    GOOD = 4
    EXCELLENT = 5

    GRADES_CHOICES = [
        (AWFUL, 1),
        (BAD, 2),
        (OKAY, 3),
        (GOOD, 4),
        (EXCELLENT, 5),
    ]

    grade = models.IntegerField(
        choices=GRADES_CHOICES,
    )
