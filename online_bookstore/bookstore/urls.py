from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = 'Inkwell Bookstore'
admin.site.site_header = 'Inkwell Bookstore Admin'
admin.site.index_title = 'Console'
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('search/', include('search.urls')),
    path('order/', include('order.urls')),
    path('', include("store.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
