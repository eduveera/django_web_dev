# customadmin/admin.py
from django.contrib import admin
from .models import MyCustomModel

@admin.register(MyCustomModel)
class MyCustomModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
