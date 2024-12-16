from django.urls import path
from . import views

app_name="posts"

urlpatterns = [
    path('', views.news_list, name="list"),
    path('post/new/', views.post_create, name='create'),
    path('post/<int:pk>/delete/', views.post_delete, name='delete')
]