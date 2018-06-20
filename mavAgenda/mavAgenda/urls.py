
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('landing/', include('landing.urls')),
    path('admin/', admin.site.urls),
]
