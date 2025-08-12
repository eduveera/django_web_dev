from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('customadmin.urls')),  
    path('dj-admin/', admin.site.urls),
    path('', include('appEdu.urls'),name="appEdu"),
]
