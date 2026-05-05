"""
URL configuration for myproject_config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Idhu mukkiam
from django.conf.urls.static import static # Idhum mukkiam

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

# Intha line thaan unga product images-ah browser-la kaattum
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)