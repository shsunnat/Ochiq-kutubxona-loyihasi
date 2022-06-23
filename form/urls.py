from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<int:pk>/', views.PostDisplay.as_view(), name='form_detail'),
    path('<int:pk>/delete/', views.FormDeleteView.as_view(), name='post_delete'),
    path('new/', views.FormCreateView.as_view(), name='form_new'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('search-blogs/', views.BlogSearchView.as_view(), name='search_blogs'),
]
