from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', include('text_to_image_generator.urls')),
]
