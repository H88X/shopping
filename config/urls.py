from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from config import settings
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.allProdCat),
    path('', include('shop.urls')),
    path('common/', include('common.urls')),
    path('cart/', include('cart.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
