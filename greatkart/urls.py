
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/',include('admin_honeypot.urls',namespace='admin_honeypot')),
    path('secureadminlogin/', admin.site.urls),
    path('',home,name="home"),
    path('store/',include('store.urls')),
    path('cart/',include('carts.urls')),
    path('accounts/',include('accounts.urls')),
    path('orders/',include('orders.urls')),
    path('contact/',include('contact.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
