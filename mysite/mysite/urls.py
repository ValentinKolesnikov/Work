from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from work import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('message/', include('message.urls')),
    path('work/', include('work.urls')),
    path('auth/', include('loginsystem.urls')),
    path('activity', views.activity),
    path('', include('mainApp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
