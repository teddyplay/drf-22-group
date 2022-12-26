from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from afisha_1 import settings




urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('movie_app.urls')),

] + static(settings.STATIC_URL, document_url=settings.STATIC_URL)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

