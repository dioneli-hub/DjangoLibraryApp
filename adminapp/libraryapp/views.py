from django.shortcuts import render, redirect
from .models import User, BorrowTransaction, Book
from .filters import UserFilter


def index(request):
    users = User.objects.all()

    myFilter = UserFilter(request.GET, queryset=users)
    users = myFilter.qs

    return render(request, "adminapp/index.html", {"users": users, "is_main_active": True, "myFilter": myFilter})


def books_list(request):
    books = Book.objects.all()
    for book in books:
        transactions = BorrowTransaction.objects.filter(book_id=book.id)
        if len(transactions) == 0 or len(transactions.filter(is_returned=False)) == 0:
            book.status = 'Доступна'
        else:
            book.status = 'Недоступна'

    return render(request, "adminapp/books_list.html", {"books": books, "is_books_active": True})


def active_books(request, id):
    user = User.objects.get(id=id)
    borrows = BorrowTransaction.objects.filter(user_id=id).filter(is_returned='False')
    books = Book.objects.filter(id__in=[borrow.book_id for borrow in borrows])
    inactive_borrows = BorrowTransaction.objects.filter(is_returned='False')
    books_available = Book.objects.exclude(id__in=[borrow.book_id for borrow in inactive_borrows])
    borrow = BorrowTransaction.objects.filter(user_id=id)

    return render(request, "adminapp/active_books.html",
                  {"user": user, "books": books, "books_available": books_available, "borrows": borrow})


def add_active_book(request, id):
    if request.method == "POST":
        user = User.objects.get(id=id)
        book_id = request.POST.get("selectedBookId")
        BorrowTransaction.objects.create(user_id=user.id, book_id=book_id, is_returned='False')
        return redirect(f'/active-books/{user.id}')
    return render(request, "adminapp/active_books.html")


def return_active_book(request, id):
    if request.method == "GET":
        active_borrow = BorrowTransaction.objects.filter(is_returned='False').get(book_id=id)
        active_borrow.is_returned = True
        active_borrow.save()
        user = User.objects.get(id=active_borrow.user_id)
        return redirect(f'/active-books/{user.id}')
    return render(request, "adminapp/active_books.html")


def book_details(request):
    return render(request, "adminapp/book_details.html")


def book_create_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('books')
    return render(request, "adminapp/books_list.html")


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
    return render(request, "adminapp/index.html")


def change_user_active_view(request, id):
    if request.method == "GET":
        user = User.objects.get(id=id)
        user.is_active = not user.is_active
        user.save()
        return redirect('home')
    return render(request, 'adminapp/index.html')
