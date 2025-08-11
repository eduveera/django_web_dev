from django.contrib import admin
from .models import Enquiry
# Register your models here.
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course', 'university', 'lead_source', 'lead_stage')
    search_fields = ('name', 'email', 'phone', 'course', 'university')
    
    
    def has_add_permission(self, request):
        return False
