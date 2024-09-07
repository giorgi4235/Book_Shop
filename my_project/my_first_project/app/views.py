from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Book, Review,Order
from .forms import MyBookForm
from django.contrib import messages

def first_view(request):
    
    books = Book.objects.all()

    response_str = ''

    for book in books:
        response_str += book.title + '\br'

    print("log",response_str)

    return HttpResponse(response_str)

# def index(request):
#     template_name = 'app/index.html'

#     books = Book.objects.all()
#     print("Books: ",books)
#     book_reviews = {}
#     for book in books:
#         reviews = Review.objects.filter(book=book)
#         book_reviews[book.id] = reviews
#         print("Books reviews: ",reviews)

    
#     context = {
#         'books': books, 
#         'book_reviews': book_reviews}

#     return render(request, template_name,context)

# {% url 'book_detail' book.id %}

def index(request):

    template_name = 'app/index.html'

    context = {
        
    }
    return render(request,template_name,context)


def books_view(request):

    books = Book.objects.all()

   
    
    template_name = 'app/books.html'

    context = {
        'books': books
    }

    return render(request,template_name,context)




    class Meta:

        model = Book
        field = ['title', 'author', 'publication_date', 'isbn','pages']




# def book_list(request):

#     template_name = 'app/book_list.html'

#     books = Book.objects.all()  # Query to get all books
#     context = {
#         'books': books
#         }
#     return render(request, template_name, context)


# def create_book(request):
#     template_name = 'app/create_book.html'
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
    
#     context = {
#         'form': form
#         }
#     return render(request, template_name,context)

def book_list_view(request):

    template_name = 'app/book_list.html'

    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request,template_name,context)

def my_books_view(request):

    template_name = 'app/my_books.html'

    books = Book.objects.filter(user=request.user)

    context = {
        'books': books
    }

    return render(request,template_name,context)
    


def create_book_view(request):

    template_name = 'app/create_book.html'

    form = MyBookForm()

    if request.POST:

        form = MyBookForm(request.POST)

     

        if form.is_valid():

            data = form.cleaned_data

            print("data: ",data)

            book = form.save(commit=False)
            book.user = request.user
            book.save()

            return redirect('my_books')
        
        else:

            print("errors: ",form.errors)


    context = {

        'form': form
    }

    return render(request,template_name,context)

def book_detail_view(request,pk):

    if request.user.status == "1":

        template_name = 'app/book_detail.html'

    else: 
        template_name = 'app/book_detail_customer.html'


    book = Book.objects.get(id=pk)

    context = {
        'book': book
    }

    return render(request,template_name,context)


def edit_book_view(request,pk):

    template_name = "app/edit_book.html"

    book = Book.objects.get(id=pk)
    form = MyBookForm(instance=book)



    if request.POST:
        form = MyBookForm(request.POST,instance=book)
        if form.is_valid():

            data = form.save()
            messages.success(request, f'Book "{book.title}" has been edited successfully.')
            print(messages)
        else:
            print(form.errors)
            messages.warning(request, f'{form.errors}')
            
    context = {

        'book': book,
        'form': form

    }

    return render(request,template_name,context)

def delete_book_view(request,pk):

    book = Book.objects.get(id=pk)

    if request.POST:

        book.delete()

        return redirect("my_books")

    return HttpResponse("waishala")



def make_order_view(request,uuid):

    if request.method == "POST":
        book = Book.objects.get(uuid=uuid)
        order = Order.objects.create(
            buyer=request.user,
            book=book,
        )

        messages.success(request, f'Book "{book.title}" has been purchased successfully.')

        return redirect("book_list")


def my_orders(request):

    template_name = "app/my_orders.html"

    if request.user.status == "1":

        orders = Order.objects.filter(book__user=request.user)

    else:

        orders = Order.objects.filter(buyer=request.user)

    context = {
        "orders": orders
    }

    return render(request,template_name,context)

    










