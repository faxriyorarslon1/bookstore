# books/views.py
from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import Q

class BookDetailView(DetailView): 
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
        Q(title__icontains=query) | Q(author__icontains=query))