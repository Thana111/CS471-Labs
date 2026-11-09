from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links', views.links_page, name="books.links"),
    path('html5/text/formatting', views.formatting_page, name="books.formatting"),
    path('html5/listing', views.listing_page, name="books.listing"),
    path('html5/tables', views.tables_page, name="books.tables"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('search', views.search),
    path('simple/query', views.simple_query, name="books.simple_query"),
    path('complex/query', views.complex_query, name="books.complex_query"),
    path('my/query', views.my_new_query, name="books.my_query"),
    path('cheap/query', views.cheap_books, name="books.cheap_query"),
]