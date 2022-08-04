
from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('store/',include('store.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
