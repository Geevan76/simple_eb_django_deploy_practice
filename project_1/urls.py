from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_1.urls')),  # app routes
    path('admin/', admin.site.urls),
]

