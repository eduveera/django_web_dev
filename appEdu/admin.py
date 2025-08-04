from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'email', 'submitted_at', 'handled_by_teacher')
    list_editable = ('handled_by_teacher',)
    list_filter = ('handled_by_teacher',)
    search_fields = ('name', 'email')
