from django.db.models import Q
from django.shortcuts import render, redirect
from .models import User, BorrowTransaction, Book


def index(request):
    users = User.objects.all()
    return render(request, "adminapp/index.html", {"users": users})


def books_list(request):
    books = Book.objects.all()
    return render(request, "adminapp/books_list.html", {"books": books})


def active_books(request, id):
    user = User.objects.get(id=id)
    borrows = BorrowTransaction.objects.filter(user_id=id)
    books = Book.objects.filter(id__in=[borrow.book_id for borrow in borrows])

    return render(request, "adminapp/active_books.html", {"user": user, "books": books})


def book_details(request):
    ###
    return render(request, "adminapp/book_details.html")


def book_create_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('books')
    context = {}
    return render(request, "adminapp/books_list.html", context)


def edit_book_view(request, id):
    try:
        book = Book.objects.get(id=id)

        if request.method == "POST":
            book.title = request.POST.get("title")
            book.author = request.POST.get("author")
            book.save()
            return redirect(f'/edit-book/{id}')
        else:
            return render(request, "adminapp/book_details.html", {"book": book})
    except Book.objects.DoesNotExist:
        return redirect('books')


def user_create_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        User.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number)
        return redirect('home')
    context = {}
    return render(request, "adminapp/index.html", context)


def user_delete_view(request, id):
    if request.method == "GET":
        object = User.objects.get(id=id)
        object.delete()
        return redirect('home')
    return render(request, 'adminapp/index.html')


def BootstrapFilterView(request):
    qs = filter(request)
    context = {
        'queryset': qs
    }
    return render(request, "active-books/<int:id>", context)


def filter(request):
    qs = Book.objects.all()
    title_or_author_query = request.GET.get('title_or_author')

    if is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(title__icontains=title_or_author_query)
                       | Q(author__icontains=title_or_author_query)
                       ).distinct()
    return qs


def is_valid_queryparam(param):
    return param != '' and param is not None
