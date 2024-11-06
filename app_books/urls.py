from django.urls import path

from app_books import views

app_name = 'books'

urlpatterns = [
    path('', views.author_list_create, name='author_list_create'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail_update_delete'),

]
