"""adminapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libraryapp import views


urlpatterns = [
    path('', views.index, name='home'),
    path('active-books/<int:id>', views.active_books, name="active-books"),
    path('books/', views.books_list, name='books'),
    path('user/<int:id>', views.active_books, name='active'),
    path('book/<int:id>', views.book_details, name='book-details'),
    path('books/create/', views.book_create_view, name='create-book'),
    path('create-user/', views.user_create_view, name='create-user'),
    path('delete-user/<int:id>', views.user_delete_view, name='delete-user'),
    path('edit-book/<int:id>', views.edit_book_view, name='edit-book'),
    path('active-books/add_active/<int:id>', views.add_active_book, name='add-active'),
    path('admin/', admin.site.urls),

]
