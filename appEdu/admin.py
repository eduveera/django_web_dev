# your_app/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Enquiry, LeadSource, LeadStage

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'lead_source', 'lead_stage_badge', 'university', 'course')
    list_filter = ('lead_source', 'lead_stage', 'university', 'course')
    search_fields = ('name', 'email', 'phone', 'university', 'course')
    ordering = ('-id',)
    list_per_page = 25

    fieldsets = (
        ("Personal Information", {
            "classes": ("wide",),
            "fields": ("name", "email", "phone", "date_of_birth"),
        }),
        ("Academic Information", {
            "classes": ("wide",),
            "fields": ("university", "course"),
        }),
        ("Lead Details", {
            "classes": ("collapse",),  # collapsed by default
            "fields": ("lead_source", "lead_stage"),
        }),
    )

    def lead_stage_badge(self, obj):
        color_map = {
            'PROSPECT': '#28a745',            # green
            'BUSY': '#fd7e14',                # orange
            'SWITCH OFF': '#6c757d',          # gray
            'DROP NOT INTERESTED': '#dc3545', # red
            'BLANK': '#007bff',               # blue
        }
        label = obj.lead_stage.name if obj.lead_stage else 'BLANK'
        color = color_map.get(label, '#6c757d')
        return format_html(
            '<span style="display:inline-block;padding:4px 10px;border-radius:6px;color:#fff;font-weight:700;font-size:11px;background:{}">{}</span>',
            color,
            label
        )
    lead_stage_badge.short_description = 'Lead Stage'
    lead_stage_badge.admin_order_field = 'lead_stage'


@admin.register(LeadSource)
class LeadSourceAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(LeadStage)
class LeadStageAdmin(admin.ModelAdmin):
    search_fields = ('name',)
