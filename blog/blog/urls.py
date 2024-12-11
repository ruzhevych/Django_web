from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('contacts/', views.contactpage),
    # path('news/', views.newspage),
    path('news/', include("posts.urls")),
    path('users/', include("users.urls")),
]
