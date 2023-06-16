from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("toon/", include('toon.urls')),
    path("user/", include('user.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    
] + static(settings.STATIC_URL, documnet_root=settings.STATIC_ROOT)
