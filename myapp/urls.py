from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>', views.book_by_id, name='book_by_id'),
    path('book/<int:pk>/edit', views.BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete', views.BookDeleteView.as_view(), name='book_delete'),
]