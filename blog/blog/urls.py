from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('contacts/', views.contactpage),
    # path('news/', views.newspage),
    path('news/', include("posts.urls")),
    path('users/', include("users.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
