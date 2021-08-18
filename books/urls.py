from django.urls import path
from .views import BookDetailView, SearchResultsListView


urlpatterns = [
    path('<uuid:pk>', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]