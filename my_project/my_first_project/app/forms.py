from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'isbn','pages']




class MyBookForm(forms.ModelForm):

    
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control" }))
    author = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    isbn = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",'type': 'number'}))
    pages = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'type': 'number'}))
    publication_date = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", 'type': 'date'}))


    class Meta:

        model = Book
        fields = ['title', 'author', 'publication_date', 'isbn','pages']
