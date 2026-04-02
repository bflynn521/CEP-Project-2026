from django.contrib import admin
from django.urls import path
from map.views import campus_map_view, carpooling_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', campus_map_view, name='campus_map'),
    path('carpooling/', carpooling_view, name='carpooling'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)