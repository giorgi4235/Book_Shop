from django.db import models
from registration.models import User
# Create your models here.
import uuid


class Book(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user',blank=True,null=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()



    def __str__(self):
        return self.title

class Review(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews',blank=True,null=True)
    review_text = models.TextField()
    rating = models.IntegerField()
    reviewer_name = models.CharField(max_length=100)
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.reviewer_name} for {self.book.title}'



class Student(models.Model):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.IntegerField()
    active = models.BooleanField()
   


class StudentProfile(models.Model):

    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)



class Order(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer',blank=True,null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book',blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)




